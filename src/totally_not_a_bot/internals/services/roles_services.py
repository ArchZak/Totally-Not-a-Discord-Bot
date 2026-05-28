import discord
import totally_not_a_bot.internals.dto.roles_dtos as roles_dto
from totally_not_a_bot.config.app import _client
from totally_not_a_bot.config.models import Role
from totally_not_a_bot.config.exceptions import GuildNotFoundError, RoleNotFoundError, MemberNotFoundError

# region Roles Tools


async def get_all_roles_service() -> list[Role]:
    """
    Get all roles and other associated information about the roles in the server.

    Args:
        None

    Returns:
        list[Role]: A list of Role objects representing the roles in the server
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    return [roles_dto._convert_role(r) for r in guild.roles]


async def get_role_by_id_service(role_id: int) -> Role | None:
    """
    Get the information about a role after passing in its id.

    Args:
        role_id (int): The ID of the role to fetch information from

    Returns:
        Role: An object representing the role in the server
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    role = guild.get_role(role_id)
    if not role:
        raise RoleNotFoundError("Role with the specified ID not found.")
    return roles_dto._convert_role(role)


async def assign_role_to_user_service(user_id: int, role_id: int):
    """
    Assign a role to a user.

    Args:
        user_id (int): The ID of the user to assign the role to
        role_id (int): The ID of the role to assign the user

    Returns:
        None
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    member = guild.get_member(user_id)
    role = guild.get_role(role_id)
    if member and role:
        await member.add_roles(role)
    else:
        if not member:
            raise MemberNotFoundError("User with the specified ID not found.")
        if not role:
            raise RoleNotFoundError("Role with the specified ID not found.")


async def remove_role_from_user_service(user_id: int, role_id: int):
    """
    Remove a role from a user.

    Args:
        user_id (int): The ID of the user to Remove the role to
        role_id (int): The ID of the role to Remove the user

    Returns:
        None
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    member = guild.get_member(user_id)
    role = guild.get_role(role_id)
    if member and role:
        await member.remove_roles(role)
    else:
        if not member:
            raise MemberNotFoundError("User with the specified ID not found.")
        if not role:
            raise RoleNotFoundError("Role with the specified ID not found.")


async def create_role_service(
    name: str, permissions: int | None = None, color: int | None = None
):
    """
    Create a new role for the server.

    Args:
        name (str): The name of the role to create
        permissions (int | None): The permissions to assign to the role, represented as a bitwise integer. If None, the role will have no permissions.
        color (int | None): The color to assign to the role, represented as an integer. If None, the role will have no color.

    Returns:
        None
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    kwargs = {"name": name}
    if permissions is not None:
        kwargs["permissions"] = discord.Permissions(permissions)
    if color is not None:
        kwargs["color"] = discord.Color(color)
    role = await guild.create_role(**kwargs)
    return roles_dto._convert_role(role)


async def edit_role_service(
    role_id: int,
    name: str | None = None,
    permissions: int | None = None,
    color: int | None = None,
):
    """
    Edit an existing role for the server.

    Args:
        role_id (int): The ID of the role to edit
        name (str | None): The new name of the role. If None, the role's name will not be changed.
        permissions (int | None): The new permissions to assign to the role, represented as a bitwise integer. If None, the role's permissions will not be changed.
        color (int | None): The new color to assign to the role, represented as an integer. If None, the role's color will not be changed.

    Returns:
        None
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
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


async def delete_role_service(role_id: int):
    """
    Delete a new role for the server.

    Args:
        role_id (int): The ID of the role to delete

    Returns:
        None
    """
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")
    role = guild.get_role(role_id)
    if role:
        await role.delete()
    else:
        raise RoleNotFoundError("Role with the specified ID not found.")


# endregion
