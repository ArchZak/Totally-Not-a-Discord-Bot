import discord
from loguru import logger


class TotallyNotABot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self):
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logger.info("Bot is ready and connected to Discord.")
