import discord

from totally_not_a_bot.config.exceptions import (
    GuildNotFoundError,
    MemberNotFoundError,
    RoleNotFoundError,
)
from totally_not_a_bot.config.models import Role
from totally_not_a_bot.server import _client


def _convert_role(role: discord.Role) -> Role:
    return Role(
        name=role.name,
        role_id=role.id,
        hoist=role.hoist,
        position=role.position,
        mentionable=role.mentionable,
        color=role.color.value if role.color else None,
    )


async def get_all_roles_in_guild() -> list[Role]:
    """Get all roles in the server as Pydantic models."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    return [_convert_role(r) for r in _client.guilds[0].roles]


async def get_role_by_id(role_id: int) -> Role | None:
    """Get a role by ID as a Pydantic model."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    role = _client.guilds[0].get_role(role_id)
    if not role:
        raise RoleNotFoundError("Role with the specified ID not found.")
    return _convert_role(role)


async def create_role(
    name: str, permissions: int | None = None, color: int | None = None
) -> Role | None:
    """Create a new role in the server."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    guild = _client.guilds[0]

    kwargs = {"name": name}
    if permissions is not None:
        kwargs["permissions"] = discord.Permissions(permissions)
    if color is not None:
        kwargs["color"] = discord.Color(color)

    role = await guild.create_role(**kwargs)
    return _convert_role(role)


async def edit_role(
    role_id: int,
    name: str | None = None,
    permissions: int | None = None,
    color: int | None = None,
):
    """Edit a role in the server."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    guild = _client.guilds[0]
    role = guild.get_role(role_id)
    if not role:
        raise RoleNotFoundError("Role with the specified ID not found.")

    kwargs = {}
    if name is not None:
        kwargs["name"] = name
    if permissions is not None:
        kwargs["permissions"] = discord.Permissions(permissions)
    if color is not None:
        kwargs["color"] = discord.Color(color)

    if kwargs:
        await role.edit(**kwargs)


async def delete_role(role_id: int):
    """Delete a role from the server."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    guild = _client.guilds[0]
    role = guild.get_role(role_id)
    if role:
        await role.delete()
    else:
        raise RoleNotFoundError("Role with the specified ID not found.")


async def assign_role_to_user(user_id: int, role_id: int):
    """Assign a role to a user."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    guild = _client.guilds[0]
    member = guild.get_member(user_id)
    role = guild.get_role(role_id)

    if member and role:
        await member.add_roles(role)
    else:
        if not member:
            raise MemberNotFoundError("User with the specified ID not found.")
        if not role:
            raise RoleNotFoundError("Role with the specified ID not found.")


async def remove_role_from_user(user_id: int, role_id: int):
    """Remove a role from a user."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    guild = _client.guilds[0]
    member = guild.get_member(user_id)
    role = guild.get_role(role_id)

    if member and role:
        await member.remove_roles(role)
    else:
        if not member:
            raise MemberNotFoundError("User with the specified ID not found.")
        if not role:
            raise RoleNotFoundError("Role with the specified ID not found.")
