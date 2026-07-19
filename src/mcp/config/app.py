import os

from dotenv import load_dotenv
from fastmcp import FastMCP

from mcp.config.discord_bot import TotallyNotABot

load_dotenv()

mcp = FastMCP("Totally-not-a-Bot")
_client = TotallyNotABot(discord_bot_guild=int(os.getenv("DISCORD_BOT_GUILD", 0)))
