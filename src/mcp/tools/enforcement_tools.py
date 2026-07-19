from typing import Annotated, Optional

from mcp.internals.services import enforcement_services


async def mute_user(
    user_id: Annotated[int, "The ID of the user to mute"],
    duration_minutes: Annotated[
        Optional[int],
        "The duration of the mute in minutes. If None, the mute will be indefinite. Defaults to None",
    ] = None,
):
    """
    Mute a user in the server, preventing them from sending messages or speaking in voice channels.

    Args:
        user_id (int): The ID of the user to mute
        duration_minutes (int, optional): The duration of the mute in minutes. If None, the mute will be indefinite. Defaults to None
    """
    return await enforcement_services.mute_user_service(user_id, duration_minutes)


async def unmute_user(
    user_id: Annotated[int, "The ID of the user to unmute"],
):
    """
    Unmute a user in the server, allowing them to send messages and speak in voice channels again.

    Args:
        user_id (int): The ID of the user to unmute
    """
    return await enforcement_services.unmute_user_service(user_id)


async def kick_user(
    user_id: Annotated[int, "The ID of the user to kick"],
    reason: Annotated[
        Optional[str], "The reason for kicking the user. Defaults to None"
    ] = None,
):
    """
    Kick a user from the server, removing them from the server but allowing them to rejoin.

    Args:
        user_id (int): The ID of the user to kick
        reason (str, optional): The reason for kicking the user. Defaults to None
    """
    return await enforcement_services.kick_user_service(user_id, reason)


async def ban_user(
    user_id: Annotated[int, "The ID of the user to ban"],
    reason: Annotated[
        Optional[str], "The reason for banning the user. Defaults to None"
    ] = None,
):
    """
    Ban a user from the server, preventing them from rejoining.

    Args:
        user_id (int): The ID of the user to ban
        reason (str, optional): The reason for banning the user. Defaults to None
    """
    return await enforcement_services.ban_user_service(user_id, reason)


async def unban_user(
    user_id: Annotated[int, "The ID of the user to unban"],
):
    """
    Unban a user from the server, allowing them to rejoin.

    Args:
        user_id (int): The ID of the user to unban
    """
    return await enforcement_services.unban_user_service(user_id)


async def move_user(
    user_id: Annotated[int, "The ID of the user to move"],
    target_channel_id: Annotated[
        int, "The ID of the target voice channel to move the user to"
    ],
):
    """
    Move a user to a different voice channel.

    Args:
        user_id (int): The ID of the user to move
        target_channel_id (int): The ID of the target voice channel to move the user to
    """
    return await enforcement_services.move_user_service(user_id, target_channel_id)


async def disconnect_user(
    user_id: Annotated[int, "The ID of the user to disconnect"],
):
    """
    Disconnect a user from their current voice channel.

    Args:
        user_id (int): The ID of the user to disconnect
    """
    return await enforcement_services.disconnect_user_service(user_id)
