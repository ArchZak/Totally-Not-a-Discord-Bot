from typing import Optional

from totally_not_a_bot.config.models import Channel

# region Channel Resources


def get_channel_info(channel_id: int) -> Channel:
    """
    Get the description, name, and other associated information about a channel in the server.

    Args:
        channel_id (int): The ID of the channel to fetch information from

    Returns:
        Channel: A Channel object containing the channel's information, such as its name, description, and other relevant details
    """


def get_all_channels_info() -> list[Channel]:
    """
    Get information about all channels in the server.

    Args:
        None

    Returns:
        list[Channel]: A list of Channel objects, each containing information about a channel in the server
    """
    pass


def get_channel_activity(channel_id: int):
    pass


def get_inactive_channels() -> list[Channel]:
    pass


# endregion

# region Channel Tools


def create_channel(name: str, channel_type: str, parent_id: Optional[int] = None):
    """
    Create a new channel in the server with the specified name, type, and optional parent category.

    Args:
        name (str): The name of the new channel
        channel_type (str): The type of the channel (e.g., "text", "voice", "category")
        parent_id (Optional[int]): The ID of the parent category for the channel, if applicable

    Returns:
        None
    """


def edit_channel(
    channel_id: int, new_name: Optional[str] = None, new_parent_id: Optional[int] = None
):
    """
    Edit the name and/or parent category of an existing channel in the server.

    Args:
        channel_id (int): The ID of the channel to edit
        new_name (Optional[str]): The new name for the channel, if changing
        new_parent_id (Optional[int]): The new parent category ID for the channel, if changing

    Returns:
        None
    """


def delete_channel(channel_id: int):
    """
    Delete an existing channel from the server.

    Args:
        channel_id (int): The ID of the channel to delete

    Returns:
        None
    """


def move_channel(channel_id: int, new_parent_id: int):
    """
    Move an existing channel to a different parent category.

    Args:
        channel_id (int): The ID of the channel to move
        new_parent_id (int): The ID of the new parent category for the channel

    Returns:
        None
    """


# endregion
