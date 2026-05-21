from datetime import datetime
from typing import Annotated, Optional

import dto.channels_dto as channels_dto
from config.models import Message

# region Message Resources


def get_recent_messages(
    channel_id: int,
    limit: int = 20,
    timestamp: Annotated[Optional[datetime], "Filter messages newer than this"] = None,
) -> list[Message]:
    """
    Fetch recent messages from a specific channel and filtered by a given timestamp, or default to the last 30 minutes worth of messages that fit the limit.

    Args:
        channel_id (int): The ID of the channel to fetch messages from
        limit (int, optional): The maximum number of messages to fetch. Defaults to 20
        timestamp (datetime, optional): Filter messages newer than this timestamp. Defaults to None

    Returns:
        list[Message]: A list of Message objects representing the recent messages in the channel
    """
    pass


def get_messages_by_filter():
    pass


def get_pinned_messages(channel_id: int) -> list[Message]:
    """
    Fetch all the pinned messages in a specific channel.

    Args:
        channel_id (int): The ID of the channel to fetch pinned messages from

    Returns:
        list[Message]: A list of Message objects representing the pinned messages in the channel
    """
    pass


def get_messages_in_context_window():
    pass


def get_threads_to_message():
    pass


def get_message_states():
    pass


# endregion

# region Message Tools


def send_message(
    channel_id: int, content: str, reply_to_message_id: Optional[int] = None
):
    """
    Send a message to a specific channel, optionally as a reply to another message.

    Args:
        channel_id (int): The ID of the channel to send the message to
        content (str): The content of the message to be sent
        reply_to_message_id (int, optional): The ID of the message to reply to. Defaults to None

    Returns:
        None
    """
    pass


def edit_message(message_id: int, new_content: str):
    """
    Edit an existing message sent by the bot.

    Args:
        message_id (int): The ID of the message to edit
        new_content (str): The new content for the message

    Returns:
        None
    """
    pass


def send_embed(
    channel_id: int, embed_data: dict, reply_to_message_id: Optional[int] = None
):
    """
    Send an embed message to a specific channel, optionally as a reply to another message.

    Args:
        channel_id (int): The ID of the channel to send the embed message to
        embed_data (dict): The data for the embed message
        reply_to_message_id (int, optional): The ID of the message to reply to. Defaults to None

    Returns:
        None
    """
    pass


def edit_embed(message_id: int, new_embed_data: dict):
    """
    Edit an existing embed message sent by the bot.

    Args:
        message_id (int): The ID of the embed message to edit
        new_embed_data (dict): The new data for the embed message

    Returns:
        None
    """
    pass


def delete_message(message_id: int):
    """
    Delete a specific message sent by the bot.

    Args:
        message_id (int): The ID of the message to delete

    Returns:
        None
    """
    pass


def add_reaction(message_id: int, emoji: str):
    """
    Add a reaction to a specific message.

    Args:
        message_id (int): The ID of the message to react to
        emoji (str): The emoji to add as a reaction

    Returns:
        None
    """
    pass


def remove_reaction(message_id: int, emoji: str):
    """
    Remove a reaction sent by the bot from a specific message.

    Args:
        message_id (int): The ID of the message to remove the reaction from
        emoji (str): The emoji to remove as a reaction

    Returns:
        None
    """
    pass


def delete_messages(message_ids: list[int]):
    """
    Delete multiple messages at once sent by the bot.

    Args:
        message_ids (list[int]): A list of message IDs to delete

    Returns:
        None
    """
    pass


async def pin_message_service(
    channel_id: int, message_id: int, reason: Optional[str] = None
):
    """
    Pin a specific message.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to pin
        reason (str, optional): The reason for pinning the message. Defaults to None

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    await message.pin(reason=reason)


async def unpin_message_service(
    channel_id: int, message_id: int, reason: Optional[str] = None
):
    """
    Unpin a specific message.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to unpin
        reason (str, optional): The reason for unpinning the message. Defaults to None

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    await message.unpin(reason=reason)


# endregion
