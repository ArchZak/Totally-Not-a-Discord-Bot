from typing import Optional

import discord

from totally_not_a_bot.config.models import Channel
from totally_not_a_bot.server import _client


def _convert_channel(channel: discord.abc.GuildChannel) -> Channel:
    return Channel(
        name=channel.name,
        channel_id=channel.id,
        channel_description=getattr(channel, "topic", None),
        channel_type=str(channel.type),
    )


def fetch_channel_by_id(channel_id: int):
    """Fetch a specific channel as a discord object. (Used internally by other services)"""
    return _client.get_channel(channel_id)


async def get_channel_info(channel_id: int) -> Channel | None:
    """Get information about a specific channel in the server."""
    channel = fetch_channel_by_id(channel_id)
    if not channel:
        return None
    return _convert_channel(channel)


async def get_all_channels_info() -> list[Channel]:
    """Get information about all channels in the server."""
    if not _client.guilds:
        return []
    return [_convert_channel(c) for c in _client.guilds[0].channels]


async def create_channel(
    name: str,
    channel_type: str,
    parent_id: Optional[int] = None,
    is_private: bool = False,
    allowed_role_ids: Optional[list[int]] = None,
):
    """Create a new channel in the server with the specified name, type, and optional parent category."""
    if not _client.guilds:
        return
    guild = _client.guilds[0]
    category = guild.get_channel(parent_id) if parent_id else None

    overwrites = {}
    if is_private:
        overwrites[guild.default_role] = discord.PermissionOverwrite(view_channel=False)

    if allowed_role_ids:
        for role_id in allowed_role_ids:
            role = guild.get_role(role_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

    channel_type_lower = channel_type.lower()
    if channel_type_lower == "voice":
        await guild.create_voice_channel(
            name=name, category=category, overwrites=overwrites if overwrites else None
        )
    elif channel_type_lower == "forum":
        await guild.create_forum(
            name=name, category=category, overwrites=overwrites if overwrites else None
        )
    else:
        await guild.create_text_channel(
            name=name, category=category, overwrites=overwrites if overwrites else None
        )


async def edit_channel(
    channel_id: int,
    new_name: Optional[str] = None,
    new_parent_id: Optional[int] = None,
    is_private: Optional[bool] = None,
    allowed_role_ids: Optional[list[int]] = None,
):
    """Edit the name, parent category, or permissions of a channel in the server."""
    channel = fetch_channel_by_id(channel_id)
    if not channel:
        return

    kwargs = {}
    if new_name is not None:
        kwargs["name"] = new_name
    if new_parent_id is not None:
        category = _client.get_channel(new_parent_id)
        kwargs["category"] = category

    if is_private is not None or allowed_role_ids is not None:
        # Fetch current overwrites to modify them
        overwrites = channel.overwrites
        guild = channel.guild

        if is_private is not None:
            if is_private:
                overwrites[guild.default_role] = discord.PermissionOverwrite(
                    view_channel=False
                )
            else:
                # remove overwrite for default role or set to None
                overwrites[guild.default_role] = discord.PermissionOverwrite(
                    view_channel=None
                )

        if allowed_role_ids is not None:
            for role_id in allowed_role_ids:
                role = guild.get_role(role_id)
                if role:
                    overwrites[role] = discord.PermissionOverwrite(view_channel=True)

        kwargs["overwrites"] = overwrites

    if kwargs:
        await channel.edit(**kwargs)


async def delete_channel(channel_id: int):
    """Delete a channel from the server."""
    channel = fetch_channel_by_id(channel_id)
    if channel:
        await channel.delete()


async def move_channel(channel_id: int, new_parent_id: int):
    """Move a channel to a different parent category."""
    channel = fetch_channel_by_id(channel_id)
    if not channel:
        return
    category = _client.get_channel(new_parent_id)
    if category:
        await channel.edit(category=category)


async def set_channel_position(channel_id: int, position: int):
    """Change the position/order of a channel."""
    channel = fetch_channel_by_id(channel_id)
    if channel:
        await channel.edit(position=position)
