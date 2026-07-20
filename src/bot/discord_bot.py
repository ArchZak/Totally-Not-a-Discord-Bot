import discord
from loguru import logger

from rag.agent import build_native_agent


class TotallyNotABot(discord.Client):
    """
    The core Discord bot client that integrates directly with a native LangChain RAG agent.
    """

    def __init__(self, discord_bot_guild: int):
        # We store the guild ID for potential future slash command registration
        self.discord_bot_guild = discord_bot_guild

        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(intents=intents)

        self.agent = None

    async def on_ready(self):
        """Called when the bot successfully connects (or reconnects) to Discord."""
        logger.info(f"Logged in: {self.user} {self.user.id}")

        # on ready can fire a couple times when reconnecting so we only want 1 agent
        if self.agent is None:
            try:
                self.agent = await build_native_agent()
                logger.info("Native LangChain Agent initialized in the Discord Bot.")
            except Exception as e:
                logger.error(f"Failed to initialize the LangChain Agent: {e}")

    async def on_message(self, message: discord.Message):
        """Called whenever a message is sent in a channel the bot can see."""
        if message.author.bot:
            return

        # send message to bot
        try:
            await self.agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": (
                                f"Channel: #{message.channel.name}\n"
                                f"Author: {message.author.display_name}\n"
                                f"Message: {message.content}"
                            ),
                        }
                    ]
                }
            )

        except Exception as _:
            logger.error(f"Error processing message")
