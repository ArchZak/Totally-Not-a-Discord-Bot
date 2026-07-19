import datetime
from typing import Optional

import discord

from mcp.config.app import _client
from mcp.config.exceptions import (
    ChannelNotFoundError,
    GuildNotFoundError,
    MemberNotFoundError,
)


async def fetch_member(user_id: int):
    guild = _client.get_guild(_client.discord_bot_guild)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    member = guild.get_member(user_id)
    if not member:
        # Try fetching if not in cache
        try:
            member = await guild.fetch_member(user_id)
        except discord.NotFound:
            member = None
    if not member:
        raise MemberNotFoundError(f"User with ID {user_id} not found in target guild.")
    return member


async def mute_user_service(
    user_id: int,
    duration_minutes: Optional[int] = None,
    reason: str = "No reason provided",
):
    member = await fetch_member(user_id)
    duration = (
        datetime.timedelta(minutes=duration_minutes) if duration_minutes else None
    )
    await member.edit(mute=True, reason=reason, timeout=duration)


async def unmute_user_service(user_id: int, reason: str = "No reason provided"):
    member = await fetch_member(user_id)
    await member.edit(mute=False, reason=reason)


async def kick_user_service(user_id: int, reason: Optional[str] = None):
    member = await fetch_member(user_id)
    await member.kick(reason=reason)


async def ban_user_service(user_id: int, reason: Optional[str] = None):
    member = await fetch_member(user_id)
    await member.ban(reason=reason)


async def unban_user_service(user_id: int):
    guild = _client.get_guild(_client.discord_bot_guild)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    try:
        user = await _client.fetch_user(user_id)
        await guild.unban(user)
    except discord.NotFound:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")


async def move_user_service(user_id: int, target_channel_id: int):
    member = await fetch_member(user_id)
    channel = _client.get_channel(target_channel_id)
    if (
        not channel
        or not isinstance(channel, discord.abc.GuildChannel)
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {target_channel_id} not found in target guild."
        )
    await member.move_to(channel)


async def disconnect_user_service(user_id: int):
    member = await fetch_member(user_id)
    await member.move_to(None)
