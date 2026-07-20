import discord

from bot.models import Category, Channel


def _convert_category(category: discord.CategoryChannel) -> Category:
    return Category(
        name=category.name,
        category_id=category.id,
        is_private=category.is_private(),
        allowed_role_ids=[
            role.id for role in category.overwrites if isinstance(role, discord.Role)
        ],
        channels=[
            Channel(
                name=channel.name,
                channel_id=channel.id,
                channel_description=channel.topic
                if isinstance(channel, discord.TextChannel)
                else None,
                channel_type=(
                    "text"
                    if isinstance(channel, discord.TextChannel)
                    else "voice"
                    if isinstance(channel, discord.VoiceChannel)
                    else "forum"
                    if isinstance(channel, discord.ForumChannel)
                    else "unknown"
                ),
            )
            for channel in category.channels
        ],
    )
