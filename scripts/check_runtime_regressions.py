#!/usr/bin/env python3
"""Check Argo retry/configuration and MCP launch fixes without API requests.

Run with the documented environment: python -B scripts/check_runtime_regressions.py
All HTTP calls are mocked, external connections are blocked, and no model is run.
"""
from __future__ import annotations

import io
import json
import logging
import os
from pathlib import Path
import runpy
import socket
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True


_ORIGINAL_SOCKET_CONNECT = socket.socket.connect


def _deny_network(*args, **kwargs):
    raise AssertionError("Network access is forbidden in the offline runtime checks")


def _allow_local_socketpair(stream, address):
    # Windows asyncio implements its internal socketpair over loopback TCP.
    if isinstance(address, tuple) and address[0] in ("127.0.0.1", "::1"):
        return _ORIGINAL_SOCKET_CONNECT(stream, address)
    return _deny_network()


class ArgoRuntimeChecks(unittest.TestCase):
    def setUp(self):
        self.enterContext(patch.object(argo_client, "API_USER", "offline-regression-check"))
        self.enterContext(patch.object(argo_client.argo_config, "ARGO_MAX_ATTEMPTS", 4, create=True))
        self.sleep = self.enterContext(patch.object(argo_client.time, "sleep"))

    @staticmethod
    def response(text=None, *, status=200):
        response = argo_client.requests.Response()
        response.status_code = status
        response._content = json.dumps({"response": text}).encode("utf-8")
        response.encoding = "utf-8"
        return response

    def test_blank_and_null_responses_retry_the_identical_request(self):
        responses = [self.response(" \n "), self.response(None), self.response("A complete answer")]
        with patch.object(argo_client, "_post_argo", side_effect=responses) as post:
            self.assertEqual(argo_client.call_argo("question", "system"), "A complete answer")
        self.assertEqual(post.call_count, 3)
        self.assertEqual(post.call_args_list[0], post.call_args_list[1])
        self.assertEqual(post.call_args_list[1], post.call_args_list[2])
        self.assertEqual(self.sleep.call_count, 2)

    def test_persistent_empty_response_fails_after_retry_budget(self):
        with patch.object(argo_client, "_post_argo", return_value=self.response("")) as post:
            with self.assertRaisesRegex(RuntimeError, "4 attempts:.*empty model response"):
                argo_client.call_argo("question", "system")
        self.assertEqual(post.call_count, 4)
        self.assertEqual(self.sleep.call_count, 3)

    def test_persistent_null_response_fails_after_retry_budget(self):
        with patch.object(argo_client, "_post_argo", return_value=self.response(None)) as post:
            with self.assertRaisesRegex(RuntimeError, "empty model response"):
                argo_client.call_argo("question", "system")
        self.assertEqual(post.call_count, 4)

    def test_nonstring_response_is_normalized(self):
        with patch.object(argo_client, "_post_argo", return_value=self.response(42)):
            self.assertEqual(argo_client.call_argo("question", "system"), "42")

    def test_authentication_failures_are_not_retried(self):
        for status in (401, 403):
            with self.subTest(status=status):
                self.sleep.reset_mock()
                with patch.object(argo_client, "_post_argo", return_value=self.response("access denied", status=status)) as post:
                    with self.assertRaisesRegex(RuntimeError, f"authentication failed.*{status}"):
                        argo_client.call_argo("question", "system")
                self.assertEqual(post.call_count, 1)
                self.sleep.assert_not_called()

    def test_missing_username_fails_before_http(self):
        for username in ("", " \t", None):
            with self.subTest(username=username):
                with patch.object(argo_client, "API_USER", username), patch.object(argo_client, "_post_argo") as post:
                    with self.assertRaisesRegex(RuntimeError, "Set ARGO_API_USER"):
                        argo_client.call_argo("question", "system")
                post.assert_not_called()

    def test_legacy_model_also_checks_username_before_http(self):
        with patch.object(argo_client, "API_USER", ""), patch.object(argo_client.requests, "post") as post:
            with self.assertRaisesRegex(RuntimeError, "Set ARGO_API_USER"):
                # Validation precedes optional LangChain setup and model imports.
                argo_client.ArgoLLM._generate(object(), [])
        post.assert_not_called()

    def test_tool_call_stop_token_is_still_completed(self):
        with patch.object(argo_client, "_post_argo", return_value=self.response('<tool_call>{"name":"search_metals"}')):
            self.assertEqual(argo_client.call_argo("question", "system"), '<tool_call>{"name":"search_metals"}</tool_call>')


class ConfigurationChecks(unittest.TestCase):
    def test_explicit_endpoint_and_username(self):
        with patch.dict(os.environ, {"ARGO_API_USER": "  researcher  ", "ARGO_API_URL": "https://example.invalid/argo"}, clear=True):
            config = runpy.run_path(str(ROOT / "argo_config.py"))
        self.assertEqual(config["API_USER"], "researcher")
        self.assertEqual(config["API_URL"], "https://example.invalid/argo")

    def test_username_does_not_default_to_a_personal_account(self):
        with patch.dict(os.environ, {}, clear=True):
            config = runpy.run_path(str(ROOT / "argo_config.py"))
        self.assertEqual(config["API_USER"], "")
        self.assertTrue(config["API_URL"].startswith("https://"))


class StdioTransportChecks(unittest.TestCase):
    def test_real_stderr_is_retained(self):
        with open(os.devnull, "w", encoding="utf-8") as stream:
            with patch.object(sys, "stderr", stream):
                self.assertIs(agent_runtime._subprocess_log_target(), stream)

    def test_stringio_stderr_uses_original_descriptor(self):
        with open(os.devnull, "w", encoding="utf-8") as original:
            with patch.object(sys, "stderr", io.StringIO()), patch.object(sys, "__stderr__", original):
                self.assertIs(agent_runtime._subprocess_log_target(), original)
                with patch.object(agent_runtime, "StdioTransport") as transport:
                    agent_runtime._build_server_transport()
                options = transport.call_args.kwargs
                self.assertIs(options["log_file"], original)
                self.assertEqual(options["command"], sys.executable)
                self.assertEqual(options["args"], ["server.py"])
                self.assertEqual(Path(options["cwd"]).resolve(), ROOT)

    def test_no_stderr_descriptor_uses_null_device(self):
        with patch.object(sys, "stderr", io.StringIO()), patch.object(sys, "__stderr__", None):
            self.assertEqual(agent_runtime._subprocess_log_target(), Path(os.devnull))

    def test_closed_stderr_descriptor_uses_null_device(self):
        stream = io.StringIO()
        stream.close()
        with patch.object(sys, "stderr", stream), patch.object(sys, "__stderr__", None):
            self.assertEqual(agent_runtime._subprocess_log_target(), Path(os.devnull))


def main() -> int:
    global argo_client, agent_runtime
    logging.disable(logging.CRITICAL)
    # Guard imports as well as tests; a missed mock cannot contact any endpoint.
    with patch.object(socket.socket, "connect", _allow_local_socketpair), patch.object(socket, "create_connection", _deny_network):
        import argo_client
        import agent_runtime
        suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
