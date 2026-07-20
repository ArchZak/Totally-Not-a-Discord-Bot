from typing import Annotated, Literal, Optional

from bot.internals.services import channels_services
from bot.models import Channel, ChannelEditParam, ChannelParam


async def get_channel_info(
    channel_id: Annotated[int, "The ID of the channel to fetch information from"],
) -> Optional[Channel]:
    """
    Get the description, name, and other associated information about a channel in the server.

    Args:
        channel_id (int): The ID of the channel to fetch information from

    Returns:
        Optional[Channel]: A Channel object containing the channel's information, such as its name, description, and other relevant details
    """
    return await channels_services.get_channel_info_service(channel_id)


async def get_all_channels_info() -> list[Channel]:
    """
    Get information about all channels in the server.

    Args:
        None

    Returns:
        list[Channel]: A list of Channel objects, each containing information about a channel in the server
    """
    return await channels_services.get_all_channels_info_service()


async def create_channel(
    name: Annotated[str, "The name of the new channel"],
    channel_type: Annotated[
        Literal["text", "voice", "forum"],
        "The type of channel to create (e.g., 'text', 'voice', 'forum')",
    ],
    parent_id: Annotated[
        Optional[int], "The ID of the parent category for the channel, if applicable"
    ] = None,
    is_private: Annotated[
        bool, "Whether the channel should be hidden from @everyone"
    ] = False,
    allowed_role_ids: Annotated[
        Optional[list[int]], "A list of role IDs allowed to view this channel"
    ] = None,
) -> int:
    """
    Create a new channel in the server with the specified name, type, and optional parent category.

    Args:
        name (str): The name of the new channel
        channel_type (str): The type of the channel (e.g., "text", "voice", "forum")
        parent_id (Optional[int]): The ID of the parent category for the channel, if applicable
        is_private (bool): Whether the channel should be hidden from @everyone
        allowed_role_ids (Optional[list[int]]): A list of role IDs allowed to view this channel

    Returns:
        channel_id (int): The ID of the newly created channel
    """
    return await channels_services.create_channel_service(
        name, channel_type, parent_id, is_private, allowed_role_ids
    )


async def bulk_create_channels(
    channels: Annotated[
        list[ChannelParam],
        "A list of dictionaries, each containing the parameters for a channel to create",
    ],
    parent_id: Annotated[
        Optional[int], "The ID of the parent category for the channels, if applicable"
    ] = None,
) -> list[int]:
    """
    Create multiple channels in the server at once based on a list of channel parameters.

    Args:
        channels (list[ChannelParam]): A list of dictionaries, each containing the parameters for a channel to create (e.g., name, type, privacy settings)
        parent_id (Optional[int]): The ID of the parent category for the channels, if applicable

    Returns:
        list[int]: A list of IDs for the newly created channels
    """
    created_channel_ids = []
    for channel in channels:
        channel_id = await create_channel(
            name=channel.name,
            channel_type=channel.channel_type,
            parent_id=parent_id,
            is_private=channel.is_private,
            allowed_role_ids=channel.allowed_role_ids,
        )
        created_channel_ids.append(channel_id)
    return created_channel_ids


async def bulk_edit_channels(
    channels: Annotated[
        list[ChannelEditParam],
        "A list of channel edit instructions, each containing a channel_id and any fields to update",
    ],
) -> None:
    """
    Edit multiple channels in the server.

    Args:
        channels (list[ChannelEditParam]): A list of channel edit instructions, each containing a channel_id and any fields to update

    Returns:
        None
    """
    for channel in channels:
        await edit_channel(
            channel_id=channel["channel_id"],
            new_name=channel.get("new_name"),
            new_parent_id=channel.get("new_parent_id"),
            is_private=channel.get("is_private"),
            allowed_role_ids=channel.get("allowed_role_ids"),
        )


async def edit_channel(
    channel_id: Annotated[int, "The ID of the channel to edit"],
    new_name: Annotated[
        Optional[str], "The new name for the channel, if changing"
    ] = None,
    new_parent_id: Annotated[
        Optional[int], "The new parent category ID for the channel, if changing"
    ] = None,
    is_private: Annotated[
        Optional[bool],
        "Whether the channel should be hidden from @everyone, if changing",
    ] = None,
    allowed_role_ids: Annotated[
        Optional[list[int]],
        "A new list of role IDs allowed to view this channel, if changing",
    ] = None,
):
    """
    Edit the properties of an existing channel, such as its name, parent category, privacy settings, and allowed roles.

    Args:
        channel_id (int): The ID of the channel to edit
        new_name (Optional[str]): The new name for the channel, if changing
        new_parent_id (Optional[int]): The new parent category ID for the channel, if changing
        is_private (Optional[bool]): Whether the channel should be hidden from @everyone, if changing
        allowed_role_ids (Optional[list[int]]): A new list of role IDs allowed to view this channel, if changing

    Returns:
        None
    """
    return await channels_services.edit_channel_service(
        channel_id, new_name, new_parent_id, is_private, allowed_role_ids
    )


async def delete_channel(channel_id: Annotated[int, "The ID of the channel to delete"]):
    """
    Delete an existing channel from the server.

    Args:
        channel_id (int): The ID of the channel to delete

    Returns:
        None
    """
    return await channels_services.delete_channel_service(channel_id)


async def bulk_delete_channels(
    channel_ids: Annotated[list[int], "A list of channel IDs to delete"],
) -> None:
    """
    Delete multiple channels from the server.

    Args:
        channel_ids (list[int]): A list of channel IDs to delete

    Returns:
        None
    """
    for channel_id in channel_ids:
        await delete_channel(channel_id)


async def move_channel(
    channel_id: Annotated[int, "The ID of the channel to move"],
    new_parent_id: Annotated[
        int, "The ID of the new parent category to move the channel under"
    ],
):
    """
    Move an existing channel to a different parent category.

    Args:
        channel_id (int): The ID of the channel to move
        new_parent_id (int): The ID of the new parent category to move the channel under

    Returns:
        None
    """
    return await channels_services.move_channel_service(channel_id, new_parent_id)


async def set_channel_position(
    channel_id: Annotated[int, "The ID of the channel to reposition"],
    position: Annotated[
        int, "The new position index for the channel within its category (0-based)"
    ],
):
    """
    Change the position/order of a channel within its category.

    Args:
        channel_id (int): The ID of the channel to reposition
        position (int): The new position index for the channel within its category (0-based)

    Returns:
        None
    """
    return await channels_services.set_channel_position_service(channel_id, position)
