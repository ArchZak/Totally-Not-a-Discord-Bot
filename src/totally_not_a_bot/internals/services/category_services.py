import discord

import totally_not_a_bot.internals.dto.category_dtos as category_dtos
import totally_not_a_bot.internals.services.channels_services as channels_services
from totally_not_a_bot.config.app import _client
from totally_not_a_bot.config.exceptions import (
    CategoryNotFoundError,
    GuildNotFoundError,
)
from totally_not_a_bot.config.models import Category, ChannelParam

# region Category Tools


async def get_category_info(category_id: int) -> Category:
    """Get the information about a category."""
    category = _client.get_channel(category_id)
    if (
        not category
        or not isinstance(category, discord.CategoryChannel)
        or category.guild.id != _client.target_guild_id
    ):
        raise CategoryNotFoundError(
            "Category with the specified ID not found in the target guild."
        )

    return category_dtos._convert_category(category)


async def get_all_categories_info_service() -> list[Category]:
    """Get all categories and their information in the server."""
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")

    return [category_dtos._convert_category(c) for c in guild.categories]


async def create_category_service(
    name: str, is_private: bool = False, allowed_role_ids: list[int] | None = None
):
    """Create a new category in the server."""
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")

    overwrites = {}
    if is_private:
        overwrites[guild.default_role] = discord.PermissionOverwrite(view_channel=False)

    if allowed_role_ids:
        for role_id in allowed_role_ids:
            role = guild.get_role(role_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

    category_made = await guild.create_category(
        name=name, overwrites=overwrites if overwrites else None
    )

    return category_made.id


async def create_category_with_channels_service(
    name: str,
    channels: list[ChannelParam],
    is_private: bool = False,
    allowed_role_ids: list[int] | None = None,
):
    """Create a new category in the server along with specified channels within it."""
    category_id = await create_category_service(name, is_private, allowed_role_ids)
    for channel in channels:
        await channels_services.create_channel_service(
            name=channel.name,
            channel_type=channel.channel_type,
            parent_id=category_id,
            is_private=is_private,
        )

    return category_id


async def edit_category_service(
    category_id: int,
    new_name: str | None = None,
    is_private: bool | None = None,
    allowed_role_ids: list[int] | None = None,
):
    """
    Edit the name or permissions of a category in the server.

    Args:
        category_id (int): The ID of the category to edit
        new_name (str | None): The new name for the category
        is_private (bool | None): Whether the category should be hidden from @everyone
        allowed_role_ids (list[int] | None): A list of role IDs allowed to view this category

    Returns:
        None
    """
    category = _client.get_channel(category_id)
    if (
        not category
        or not isinstance(category, discord.CategoryChannel)
        or category.guild.id != _client.target_guild_id
    ):
        raise CategoryNotFoundError(
            "Category with the specified ID not found in the target guild."
        )

    kwargs = {}
    if new_name is not None:
        kwargs["name"] = new_name

    if is_private is not None or allowed_role_ids is not None:
        overwrites = category.overwrites
        guild = category.guild

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
        await category.edit(**kwargs)


async def delete_category_service(category_id: int):
    """
    Delete a category from the server.

    Args:
        category_id (int): The ID of the category to delete

    Returns:
        None
    """
    category = _client.get_channel(category_id)
    if (
        not category
        or not isinstance(category, discord.CategoryChannel)
        or category.guild.id != _client.target_guild_id
    ):
        raise CategoryNotFoundError(
            "Category with the specified ID not found in the target guild."
        )

    await category.delete()


async def move_category_service(category_id: int, new_position: int):
    """
    Move a category to a new position in the server.

    Args:
        category_id (int): The ID of the category to move
        new_position (int): The new position for the category
    """
    category = _client.get_channel(category_id)
    if (
        not category
        or not isinstance(category, discord.CategoryChannel)
        or category.guild.id != _client.target_guild_id
    ):
        raise CategoryNotFoundError(
            "Category with the specified ID not found in the target guild."
        )

    await category.edit(position=new_position)


# endregion
