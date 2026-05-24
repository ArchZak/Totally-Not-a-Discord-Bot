from datetime import datetime, timedelta
from typing import Annotated, Optional

import dto.channels_dto as channels_dto
import dto.users_dtos as users_dto
from config.exceptions import MessageOwnershipError
from config.models import Embed, Message
from discord import Emoji, PartialEmoji, Reaction

# region Message Resources


async def get_recent_messages_service(
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
    channel = channels_dto.fetch_channel_by_id(channel_id)
    if timestamp is None:
        timestamp = datetime.now(datetime.timezone.utc) - timedelta(minutes=30)
    return [
        Message(
            content=msg.content,
            author_id=msg.author.id,
            channel_id=msg.channel.id,
            timestamp=msg.created_at.isoformat(),
        )
        async for msg in channel.history(limit=limit, after=timestamp)
    ]


def get_messages_by_filter_service():
    """Not sure how to implement this yet"""
    pass


async def get_pinned_messages_service(channel_id: int) -> list[Message]:
    """
    Fetch all the pinned messages in a specific channel.

    Args:
        channel_id (int): The ID of the channel to fetch pinned messages from

    Returns:
        list[Message]: A list of Message objects representing the pinned messages in the channel
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    return [
        Message(
            content=msg.content,
            author_id=msg.author.id,
            channel_id=msg.channel.id,
            timestamp=msg.created_at.isoformat(),
        )
        async for msg in channel.pins()
    ]


async def get_messages_in_context_window_service(
    channel_id: int, message_id: int, window_size: int = 5
) -> list[Message]:
    pass


async def get_threads_from_message_service(
    channel_id: int, message_id: int
) -> list[Message]:
    """
    Fetch all threads that have been started from a specific message.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to fetch threads from

    Returns:
        list[Message]: A list of Message objects representing the threads started from the specified message
    """


async def get_message_states_service():
    pass


# endregion

# region Message Tools


async def send_message_service(
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
    channel = channels_dto.fetch_channel_by_id(channel_id)
    if reply_to_message_id:
        message_to_reply_to = await channel.fetch_message(reply_to_message_id)
        await message_to_reply_to.reply(content)
    else:
        await channel.send(content)


async def edit_message_service(channel_id: int, message_id: int, new_content: str):
    """
    Edit an existing message sent by the bot.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to edit
        new_content (str): The new content for the message

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    if message.author.id == channels_dto.get_bot_id_dto():
        await message.edit(content=new_content)
    else:
        raise MessageOwnershipError("You can only edit messages sent by the bot.")


async def delete_message_service(channel_id: int, message_id: int):
    """
    Delete a specific message sent by the bot.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to delete

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    if message.author.id == users_dto.get_bot_id_dto():
        await message.delete()
    else:
        raise MessageOwnershipError("You can only delete messages sent by the bot.")


async def send_embed_service(
    channel_id: int, embed_data: Embed, reply_to_message_id: Optional[int] = None
):
    """
    Send an embed message to a specific channel, optionally as a reply to another message.

    Args:
        channel_id (int): The ID of the channel to send the embed message to
        embed_data (Embed): The embed data for the message
        reply_to_message_id (int, optional): The ID of the message to reply to. Defaults to None

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    if reply_to_message_id:
        message_to_reply_to = await channel.fetch_message(reply_to_message_id)
        await message_to_reply_to.reply(embed=embed_data.model_dump())
    else:
        await channel.send(embed=embed_data.model_dump())


async def edit_embed_service(channel_id: int, message_id: int, new_embed_data: Embed):
    """
    Edit an existing embed message sent by the bot.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the embed message to edit
        new_embed_data (Embed): The new embed data for the message

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    if message.author.id == users_dto.get_bot_id_dto():
        await message.edit(embed=new_embed_data.model_dump())
    else:
        raise MessageOwnershipError("You can only edit messages sent by the bot.")


async def add_reaction_service(
    channel_id: int,
    message_id: int,
    emoji: Annotated[str, Emoji, PartialEmoji, Reaction, "the emoji to add"],
):
    """
    Add a reaction to a specific message.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to react to
        emoji (str): The emoji to add as a reaction

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    await message.add_reaction(emoji)


async def remove_reaction_service(
    channel_id: int,
    message_id: int,
    emoji: Annotated[str, Emoji, PartialEmoji, Reaction, "the emoji to remove"],
):
    """
    Remove a reaction sent by the bot from a specific message.

    Args:
        channel_id (int): The ID of the channel containing the message
        message_id (int): The ID of the message to remove the reaction from
        emoji (str): The emoji to remove as a reaction

    Returns:
        None
    """
    channel = channels_dto.fetch_channel_by_id(channel_id)
    message = await channel.fetch_message(message_id)
    await message.remove_reaction(emoji)


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
