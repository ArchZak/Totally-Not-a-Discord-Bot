from typing import Literal, Optional

import discord

import mcp.internals.dto.channels_dto as channels_dto
from mcp.config.app import _client
from mcp.config.exceptions import (
    CategoryNotFoundError,
    ChannelNotFoundError,
    GuildNotFoundError,
)
from mcp.config.models import Channel

# region Channel Tools


def _get_category_or_raise(
    guild: discord.Guild, category_id: int
) -> discord.CategoryChannel:
    category = guild.get_channel(category_id)
    if (
        not category
        or not isinstance(category, discord.CategoryChannel)
        or getattr(category.guild, "id", None) != _client.discord_bot_guild
    ):
        raise CategoryNotFoundError(
            "Category with the specified ID not found in the target guild."
        )
    return category


def _build_channel_overwrites(
    guild: discord.Guild,
    parent_category: discord.CategoryChannel | None,
    is_private: bool,
    allowed_role_ids: Optional[list[int]],
) -> dict:
    overwrites = dict(parent_category.overwrites) if parent_category else {}

    if is_private:
        overwrites[guild.default_role] = discord.PermissionOverwrite(view_channel=False)

    if allowed_role_ids:
        for role_id in allowed_role_ids:
            role = guild.get_role(role_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

    return overwrites


async def get_channel_info_service(channel_id: int) -> Optional[Channel]:
    channel = _client.get_channel(channel_id)
    if (
        not channel
        or not isinstance(channel, discord.abc.GuildChannel)
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            "Channel with the specified ID not found in the target guild."
        )
    return channels_dto._convert_channel(channel)


async def get_all_channels_info_service() -> list[Channel]:
    guild = _client.get_guild(_client.discord_bot_guild)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    return [channels_dto._convert_channel(c) for c in guild.channels]


async def create_channel_service(
    name: str,
    channel_type: Literal["text", "voice", "forum"] | str,
    parent_id: Optional[int] = None,
    is_private: bool = False,
    allowed_role_ids: Optional[list[int]] = None,
) -> int:
    guild = _client.get_guild(_client.discord_bot_guild)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")

    category = _get_category_or_raise(guild, parent_id) if parent_id else None
    overwrites = _build_channel_overwrites(
        guild, category, is_private, allowed_role_ids
    )

    channel_type_lower = str(channel_type).lower()
    if channel_type_lower == "voice":
        channel = await guild.create_voice_channel(
            name=name, category=category, overwrites=overwrites if overwrites else None
        )
    elif channel_type_lower == "forum":
        channel = await guild.create_forum(
            name=name, category=category, overwrites=overwrites if overwrites else None
        )
    else:
        channel = await guild.create_text_channel(
            name=name, category=category, overwrites=overwrites if overwrites else None
        )

    return channel.id


async def edit_channel_service(
    channel_id: int,
    new_name: Optional[str] = None,
    new_parent_id: Optional[int] = None,
    is_private: Optional[bool] = None,
    allowed_role_ids: Optional[list[int]] = None,
):
    channel = _client.get_channel(channel_id)
    if (
        not channel
        or not isinstance(channel, discord.abc.GuildChannel)
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            "Channel with the specified ID not found in the target guild."
        )

    kwargs = {}
    if new_name is not None:
        kwargs["name"] = new_name
    if new_parent_id is not None:
        category = _get_category_or_raise(channel.guild, new_parent_id)
        kwargs["category"] = category

    if is_private is not None or allowed_role_ids is not None:
        overwrites = channel.overwrites
        guild = channel.guild

        if is_private is not None:
            if is_private:
                overwrites[guild.default_role] = discord.PermissionOverwrite(
                    view_channel=False
                )
            else:
                overwrites[guild.default_role] = discord.PermissionOverwrite(
                    view_channel=None
                )

        if allowed_role_ids is not None:
            for role_id in allowed_role_ids:
                role = guild.get_role(role_id)
                if role:
                    overwrites[role] = discord.PermissionOverwrite(view_channel=True)

        kwargs["overwrites"] = overwrites

    if kwargs:
        await channel.edit(**kwargs)


async def delete_channel_service(channel_id: int):
    channel = _client.get_channel(channel_id)
    if (
        not channel
        or not isinstance(channel, discord.abc.GuildChannel)
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            "Channel with the specified ID not found in the target guild."
        )
    await channel.delete()


async def move_channel_service(channel_id: int, new_parent_id: int):
    channel = _client.get_channel(channel_id)
    if (
        not channel
        or not isinstance(channel, discord.abc.GuildChannel)
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            "Channel with the specified ID not found in the target guild."
        )

    category = _get_category_or_raise(channel.guild, new_parent_id)
    await channel.edit(category=category)


async def set_channel_position_service(channel_id: int, position: int):
    channel = _client.get_channel(channel_id)
    if (
        not channel
        or not isinstance(channel, discord.abc.GuildChannel)
        or getattr(channel.guild, "id", None) != _client.discord_bot_guild
    ):
        raise ChannelNotFoundError(
            "Channel with the specified ID not found in the target guild."
        )

    await channel.edit(position=position)


# endregion
