import discord

from bot.models import Role


def _convert_role(role: discord.Role) -> Role:
    return Role(
        name=role.name,
        role_id=role.id,
        hoist=role.hoist,
        position=role.position,
        mentionable=role.mentionable,
        color=role.color.value if role.color else None,
    )
