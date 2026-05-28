import datetime

import totally_not_a_bot.internals.dto.channels_dto as channels_dto
import totally_not_a_bot.internals.dto.users_dtos as users_dtos
from totally_not_a_bot.config.exceptions import (
    ChannelNotFoundError,
    MemberNotFoundError,
)


async def mute_user_dto(user_id: int, duration_minutes: int, reason: str):
    """DTO for muting a user in the server, preventing them from sending messages and speaking in voice channels."""

    duration = datetime.timedelta(minutes=duration_minutes)

    member = users_dtos.fetch_user_by_id(user_id)
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    await member.edit(mute=True, reason=reason, timeout=duration)


async def unmute_user_dto(user_id: int, reason: str):
    """DTO for unmuting a user in the server, allowing them to send messages and speak in voice channels again."""
    member = users_dtos.fetch_user_by_id(user_id)
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    await member.edit(mute=False, reason=reason)


async def kick_user_dto(user_id: int, reason: str):
    """DTO for kicking a user from the server, removing them from the server but allowing them to rejoin."""
    member = users_dtos.fetch_user_by_id(user_id)
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    await member.kick(reason=reason)


async def ban_user_dto(user_id: int, reason: str):
    """DTO for banning a user from the server, preventing them from rejoining."""
    member = users_dtos.fetch_user_by_id(user_id)
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    await member.ban(reason=reason)


async def unban_user_dto(user_id: int):
    """DTO for unbanning a user from the server, allowing them to rejoin."""
    member = users_dtos.fetch_user_by_id(user_id)
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    await member.unban()


async def move_user_to_voice_channel_dto(user_id: int, channel_id: int):
    """DTO for moving a user to a specific voice channel."""
    member = users_dtos.fetch_user_by_id(user_id)
    channel = channels_dto.fetch_channel_by_id(channel_id)
    if channel is None:
        raise ChannelNotFoundError(f"Channel with ID {channel_id} not found.")
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")

    await member.move_to(channel_id)


async def disconnect_user_from_voice_channel_dto(user_id: int):
    """DTO for disconnecting a user from their current voice channel."""
    member = users_dtos.fetch_user_by_id(user_id)
    if member is None:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    await member.move_to(None)
