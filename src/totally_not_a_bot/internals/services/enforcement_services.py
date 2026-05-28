from typing import Optional


async def mute_user_service(user_id: int, duration_seconds: Optional[int] = None):
    """
    Mute a user in the server, preventing them from sending messages or speaking in voice channels.

    Args:
        user_id (int): The ID of the user to mute
        duration_seconds (int, optional): The duration of the mute in seconds. If None, the mute will be indefinite. Defaults to None

    Returns:
        None
    """


async def unmute_user_service(user_id: int):
    """
    Unmute a user in the server, allowing them to send messages and speak in voice channels again.

    Args:
        user_id (int): The ID of the user to unmute

    Returns:
        None
    """


async def kick_user_service(user_id: int, reason: Optional[str] = None):
    """
    Kick a user from the server, removing them from the server but allowing them to rejoin.

    Args:
        user_id (int): The ID of the user to kick
        reason (str, optional): The reason for kicking the user. Defaults to None

    Returns:
        None
    """


async def ban_user_service(user_id: int, reason: Optional[str] = None):
    """
    Ban a user from the server, preventing them from rejoining.

    Args:
        user_id (int): The ID of the user to ban
        reason (str, optional): The reason for banning the user. Defaults to None

    Returns:
        None
    """


async def unban_user_service(user_id: int):
    """
    Unban a user from the server, allowing them to rejoin.

    Args:
        user_id (int): The ID of the user to unban

    Returns:
        None
    """


async def move_user_service(user_id: int, target_channel_id: int):
    """
    Move a user to a different voice channel.

    Args:
        user_id (int): The ID of the user to move
        target_channel_id (int): The ID of the target voice channel to move the user to

    Returns:
        None
    """


async def disconnect_user_service(user_id: int):
    """
    Disconnect a user from their current voice channel.

    Args:
        user_id (int): The ID of the user to disconnect

    Returns:
        None
    """
