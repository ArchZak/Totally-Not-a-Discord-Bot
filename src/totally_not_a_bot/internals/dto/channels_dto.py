import discord

from totally_not_a_bot.config.models import Channel


def _convert_channel(channel: discord.abc.GuildChannel) -> Channel:
    return Channel(
        name=channel.name,
        channel_id=channel.id,
        channel_description=getattr(channel, "topic", None),
        channel_type=str(channel.type),
    )
