import os

from dotenv import load_dotenv
from fastmcp import FastMCP

from totally_not_a_bot.config.discord_bot import TotallyNotABot

load_dotenv()

mcp = FastMCP("Totally-not-a-Bot")
_client = TotallyNotABot(target_guild_id=int(os.getenv("TARGET_GUILD_ID", 0)))
