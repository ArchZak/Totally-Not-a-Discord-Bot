import asyncio
import os
import sys

from config.discord_bot import TotallyNotABot
from dotenv import load_dotenv
from fastmcp import FastMCP
from loguru import logger

# Redirect loguru to stderr to avoid breaking MCP stdio transport
logger.remove()
logger.add(sys.stderr, level="INFO")

mcp = FastMCP("Totally-not-a-Bot")
_client = TotallyNotABot()


async def main():
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")

    if not token:
        logger.error("Missing DISCORD_BOT_TOKEN in .env")
        return

    # Spin up discord bot on nonblocking thread using start
    asyncio.create_task(_client.start(token))
    logger.info("Spinning up Discord Bot")

    try:
        # Run MCP server on main thread over stdio
        logger.info("MCP Server starting over stdio")
        await mcp.run_async(transport="stdio")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        # Gracefully shutdown the bot
        await _client.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
