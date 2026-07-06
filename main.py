#!/usr/bin/env python
"""
SRD-46 MCP Server – entry point.

Usage
-----
    python main.py              # stdio transport (default, for MCP clients)
    python main.py --sse        # SSE transport  (for web/HTTP clients)
"""

import sys


def main():
    from server import mcp          # deferred import keeps module-level fast

    transport = "sse" if "--sse" in sys.argv else "stdio"
    print(f"Starting SRD-46 MCP server (transport={transport}) …")
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
