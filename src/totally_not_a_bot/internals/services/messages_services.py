from datetime import datetime, timedelta
from typing import Optional

import discord

import totally_not_a_bot.internals.dto.channels_dto as channels_dto
from totally_not_a_bot.config.app import _client
from totally_not_a_bot.config.exceptions import (
    ChannelNotFoundError,
    MessageNotFoundError,
    MessageOwnershipError,
)
from totally_not_a_bot.config.models import Embed, Message

# region Message Tools


async def get_recent_messages_service(
    channel_id: int,
    limit: int = 20,
    timestamp: Optional[datetime] = None,
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    if timestamp is None:
        timestamp = datetime.now(datetime.timezone.utc) - timedelta(minutes=30)
    return [
        Message(
            content=msg.content,
            author_id=msg.author.id,
            channel_id=msg.channel.id,
            timestamp=msg.created_at,
        )
        async for msg in channel.history(limit=limit, after=timestamp)
    ]


async def get_pinned_messages_service(channel_id: int) -> list[Message]:
    """
    Fetch all the pinned messages in a specific channel.

    Args:
        channel_id (int): The ID of the channel to fetch pinned messages from

    Returns:
        list[Message]: A list of Message objects representing the pinned messages in the channel
    """
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    return [
        Message(
            content=msg.content,
            author_id=msg.author.id,
            channel_id=msg.channel.id,
            timestamp=msg.created_at,
        )
        async for msg in channel.pins()
    ]


async def get_thread_from_message_service(
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")

    if not message.thread:
        return []

    return [
        Message(
            content=msg.content,
            author_id=msg.author.id,
            channel_id=msg.channel.id,
            timestamp=msg.created_at,
        )
        async for msg in message.thread.history(limit=None)
    ]


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
    if channel is None:
        raise ChannelNotFoundError(f"Channel with ID {channel_id} not found.")
    if reply_to_message_id:
        message_to_reply_to = await channel.fetch_message(reply_to_message_id)
        if message_to_reply_to is None:
            raise MessageNotFoundError(
                f"Message with ID {reply_to_message_id} not found."
            )
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")
    if _client.user and message.author.id == _client.user.id:
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")

    if _client.user and message.author.id == _client.user.id:
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
    channel = _client.get_channel(channel_id)
    d_embed = discord.Embed.from_dict(embed_data.model_dump(exclude_unset=True))
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    if reply_to_message_id:
        message_to_reply_to = await channel.fetch_message(reply_to_message_id)
        if message_to_reply_to is None:
            raise MessageNotFoundError(
                f"Message with ID {reply_to_message_id} not found."
            )
        await message_to_reply_to.reply(embed=d_embed)
    else:
        await channel.send(embed=d_embed)


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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")
    if _client.user and message.author.id == _client.user.id:
        d_embed = discord.Embed.from_dict(new_embed_data.model_dump(exclude_unset=True))
        await message.edit(embed=d_embed)
    else:
        raise MessageOwnershipError("You can only edit messages sent by the bot.")


async def add_reaction_service(
    channel_id: int,
    message_id: int,
    emoji: str,
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")
    await message.add_reaction(emoji)


async def remove_reaction_service(
    channel_id: int,
    message_id: int,
    emoji: str,
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")
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
    channel = _client.get_channel(channel_id)
    if (
        channel is None
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            f"Channel with ID {channel_id} not found in target guild."
        )
    message = await channel.fetch_message(message_id)
    if message is None:
        raise MessageNotFoundError(f"Message with ID {message_id} not found.")
    await message.unpin(reason=reason)


# endregion
