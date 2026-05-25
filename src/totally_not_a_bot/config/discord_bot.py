import discord
from loguru import logger


class TotallyNotABot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def on_ready(self):
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logger.info("Bot is ready and connected to Discord.")


# TODO investigate intents for discord.py
# TODO discord bot to have heartbeats
