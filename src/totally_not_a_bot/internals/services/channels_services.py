from typing import Annotated, Literal, Optional

import totally_not_a_bot.internals.dto.channels_dto as channels_dto
from totally_not_a_bot.config.models import Channel

# region Channel Resources


async def get_channel_info(channel_id: int) -> Optional[Channel]:
    """
    Get the description, name, and other associated information about a channel in the server.

    Args:
        channel_id (int): The ID of the channel to fetch information from

    Returns:
        Optional[Channel]: A Channel object containing the channel's information, such as its name, description, and other relevant details
    """
    return await channels_dto.get_channel_info(channel_id)


async def get_all_channels_info() -> list[Channel]:
    """
    Get information about all channels in the server.

    Args:
        None

    Returns:
        list[Channel]: A list of Channel objects, each containing information about a channel in the server
    """
    return await channels_dto.get_all_channels_info()


async def get_inactive_channels() -> list[Channel]:
    pass


# endregion

# region Channel Tools


async def create_channel(
    name: str,
    channel_type: Annotated[
        Literal["text", "voice", "forum"],
        "The type of channel to create (e.g., 'text', 'voice', 'forum')",
    ],
    parent_id: Optional[int] = None,
    is_private: bool = False,
    allowed_role_ids: Optional[list[int]] = None,
):
    """
    Create a new channel in the server with the specified name, type, and optional parent category.

    Args:
        name (str): The name of the new channel
        channel_type (str): The type of the channel (e.g., "text", "voice", "forum")
        parent_id (Optional[int]): The ID of the parent category for the channel, if applicable
        is_private (bool): Whether the channel should be hidden from @everyone
        allowed_role_ids (Optional[list[int]]): A list of role IDs allowed to view this channel

    Returns:
        None
    """
    await channels_dto.create_channel(
        name, channel_type, parent_id, is_private, allowed_role_ids
    )


async def edit_channel(
    channel_id: int,
    new_name: Optional[str] = None,
    new_parent_id: Optional[int] = None,
    is_private: Optional[bool] = None,
    allowed_role_ids: Optional[list[int]] = None,
):
    """
    Edit the name, parent category, or permissions of an existing channel in the server.

    Args:
        channel_id (int): The ID of the channel to edit
        new_name (Optional[str]): The new name for the channel, if changing
        new_parent_id (Optional[int]): The new parent category ID for the channel, if changing
        is_private (Optional[bool]): Whether the channel should be hidden from @everyone
        allowed_role_ids (Optional[list[int]]): A list of role IDs allowed to view this channel

    Returns:
        None
    """
    await channels_dto.edit_channel(
        channel_id, new_name, new_parent_id, is_private, allowed_role_ids
    )


async def delete_channel(channel_id: int):
    """
    Delete an existing channel from the server.

    Args:
        channel_id (int): The ID of the channel to delete

    Returns:
        None
    """
    await channels_dto.delete_channel(channel_id)


async def move_channel(channel_id: int, new_parent_id: int):
    """
    Move an existing channel to a different parent category.

    Args:
        channel_id (int): The ID of the channel to move
        new_parent_id (int): The ID of the new parent category for the channel

    Returns:
        None
    """
    await channels_dto.move_channel(channel_id, new_parent_id)


async def set_channel_position(channel_id: int, position: int):
    """
    Change the position/order of a channel within its category.

    Args:
        channel_id (int): The ID of the channel to move
        position (int): The new position/order for the channel

    Returns:
        None
    """
    await channels_dto.set_channel_position(channel_id, position)


# endregion
