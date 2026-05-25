import discord

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
        return []
    return [_convert_role(r) for r in _client.guilds[0].roles]


async def get_role_by_id(role_id: int) -> Role | None:
    """Get a role by ID as a Pydantic model."""
    if not _client.guilds:
        return None
    role = _client.guilds[0].get_role(role_id)
    return _convert_role(role) if role else None
