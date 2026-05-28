from typing import Optional


async def mute_user_dto(user_id: int, duration_seconds: Optional[int] = None):
    """DTO for muting a user in the server, preventing them from sending messages and speaking in voice channels."""


async def unmute_user_dto(user_id: int):
    """DTO for unmuting a user in the server, allowing them to send messages and speak in voice channels again."""


async def kick_user_dto(user_id: int, reason: Optional[str] = None):
    """DTO for kicking a user from the server, removing them from the server but allowing them to rejoin."""


async def ban_user_dto(user_id: int, reason: Optional[str] = None):
    """DTO for banning a user from the server, preventing them from rejoining."""


async def unban_user_dto(user_id: int):
    """DTO for unbanning a user from the server, allowing them to rejoin."""


async def move_user_to_voice_channel_dto(user_id: int, channel_id: int):
    """DTO for moving a user to a specific voice channel."""


async def disconnect_user_from_voice_channel_dto(user_id: int):
    """DTO for disconnecting a user from their current voice channel."""
