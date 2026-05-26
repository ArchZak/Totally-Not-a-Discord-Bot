from typing import Annotated

from totally_not_a_bot.config.models import Embed, Message
from totally_not_a_bot.internals.services import messages_services


async def get_recent_messages(
    channel_id: int, limit: int = 20, timestamp: str = None
) -> list[Message]:
    """
    Fetch recent messages from a specific channel and filtered by a given timestamp, or default to the last 30 minutes worth of messages that fit the limit.

    Args:
        channel_id (int): The ID of the channel to fetch messages from
        limit (int, optional): The maximum number of messages to fetch. Defaults to 20
        timestamp (str, optional): Filter messages newer than this timestamp in ISO format. Defaults to None

    Returns:
        list[Message]: A list of Message objects representing the recent messages in the channel
    """
    return await messages_services.get_recent_messages_service(
        channel_id, limit, timestamp
    )


async def get_pinned_messages(channel_id: int) -> list[Message]:
    """
    Fetch all the pinned messages in a specific channel.

    Args:
        channel_id (int): The ID of the channel to fetch pinned messages from

    Returns:
        list[Message]: A list of Message objects representing the pinned messages in the channel
    """
    return await messages_services.get_pinned_messages_service(channel_id)


async def get_thread_from_message(channel_id: int, message_id: int) -> list[Message]:
    """
    Fetch all threads that have been started from a specific message.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to fetch threads from

    Returns:
        list[Message]: A list of Message objects representing the threads started from the specified message
    """
    return await messages_services.get_thread_from_message_service(
        channel_id, message_id
    )


async def send_message(channel_id: int, content: str, reply_to_message_id: int = None):
    """
    Send a message to a specific channel, optionally as a reply to another message.

    Args:
        channel_id (int): The ID of the channel to send the message to
        content (str): The content of the message to be sent
        reply_to_message_id (int, optional): The ID of the message to reply to. Defaults to None
    """
    return await messages_services.send_message_service(
        channel_id, content, reply_to_message_id
    )


async def edit_message(channel_id: int, message_id: int, new_content: str):
    """
    Edit an existing message in a specific channel.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to be edited
        new_content (str): The new content to replace the existing message content
    """
    return await messages_services.edit_message_service(
        channel_id, message_id, new_content
    )


async def delete_message(channel_id: int, message_id: int):
    """
    Delete an existing message in a specific channel.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to be deleted
    """
    return await messages_services.delete_message_service(channel_id, message_id)


async def send_embed(channel_id: int, embed: Embed, reply_to_message_id: int = None):
    """
    Send an embed message to a specific channel, optionally as a reply to another message.

    Args:
        channel_id (int): The ID of the channel to send the embed message to
        embed (Embed): The Embed object containing the embed message details
        reply_to_message_id (int, optional): The ID of the message to reply to. Defaults to None
    """
    return await messages_services.send_embed_service(
        channel_id, embed, reply_to_message_id
    )


async def edit_embed(channel_id: int, message_id: int, new_embed: Embed):
    """
    Edit an existing embed message in a specific channel.

    Args:
        channel_id (int): The ID of the channel where the embed message is located
        message_id (int): The ID of the embed message to be edited
        new_embed (Embed): The new Embed object containing the updated embed message details
    """
    return await messages_services.edit_embed_service(channel_id, message_id, new_embed)


async def pin_message(channel_id: int, message_id: int):
    """
    Pin a specific message in a channel.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to be pinned
    """
    return await messages_services.pin_message_service(channel_id, message_id)


async def unpin_message(channel_id: int, message_id: int):
    """
    Unpin a specific message in a channel.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to be unpinned
    """
    return await messages_services.unpin_message_service(channel_id, message_id)


async def add_reaction(
    channel_id: int,
    message_id: int,
    emoji: str,
):
    """
    Add a reaction to a specific message in a channel.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to add a reaction to
        emoji (str): The emoji to be added as a reaction
    """
    return await messages_services.add_reaction_service(channel_id, message_id, emoji)


async def remove_reaction(
    channel_id: int,
    message_id: int,
    emoji: str,
):
    """
    Remove a reaction from a specific message in a channel.

    Args:
        channel_id (int): The ID of the channel where the message is located
        message_id (int): The ID of the message to remove a reaction from
        emoji (str): The emoji to be removed from the reactions
    """
    return await messages_services.remove_reaction_service(
        channel_id, message_id, emoji
    )
