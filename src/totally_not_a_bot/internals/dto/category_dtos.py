import discord

from totally_not_a_bot.config.models import Category
from totally_not_a_bot.server import _client


def _convert_category(category: discord.CategoryChannel) -> Category:
    return Category(
        name=category.name,
        category_id=category.id,
        is_private=category.is_private(),
        allowed_role_ids=[
            role.id for role in category.overwrites if isinstance(role, discord.Role)
        ],
    )


def fetch_category_by_id(category_id: int):
    """Fetch a specific category as a discord object."""
    return _client.get_channel(category_id)


async def get_all_categories_info() -> list[Category]:
    """Get information about all categories in the server."""
    if not _client.guilds:
        return []
    return [_convert_category(c) for c in _client.guilds[0].categories]


async def create_category(
    name: str, is_private: bool = False, allowed_role_ids: list[int] | None = None
):
    """Create a new category in the server with the specified name."""
    if not _client.guilds:
        return
    guild = _client.guilds[0]

    overwrites = {}
    if is_private:
        overwrites[guild.default_role] = discord.PermissionOverwrite(view_channel=False)

    if allowed_role_ids:
        for role_id in allowed_role_ids:
            role = guild.get_role(role_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True)

    await guild.create_category(
        name=name, overwrites=overwrites if overwrites else None
    )


async def edit_category(
    category_id: int,
    new_name: str | None = None,
    is_private: bool | None = None,
    allowed_role_ids: list[int] | None = None,
):
    """Edit the name or permissions of a category in the server."""
    category = fetch_category_by_id(category_id)
    if not category:
        return

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


async def delete_category(category_id: int):
    """Delete a category from the server."""
    category = fetch_category_by_id(category_id)
    if category:
        await category.delete()


async def move_category(category_id: int, new_position: int):
    """Move a category to a new position in the server's channel list."""
    category = fetch_category_by_id(category_id)
    if category:
        await category.edit(position=new_position)
