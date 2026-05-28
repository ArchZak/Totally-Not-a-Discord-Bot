from typing import Optional

import discord

from totally_not_a_bot.config.app import _client
from totally_not_a_bot.config.exceptions import (
    GuildNotFoundError,
    MemberNotFoundError,
)
from totally_not_a_bot.config.models import Embed, Member


def _convert_member(member: discord.Member) -> Member:
    return Member(
        user_id=member.id,
        nickname=member.nick,
        roles=[role.id for role in member.roles],
        date_joined=member.joined_at,
    )


def get_bot_id_dto() -> int:
    """Get the bot's user ID."""
    if _client.user:
        return _client.user.id
    else:
        raise MemberNotFoundError("Bot user not found.")


def fetch_user_by_id(user_id: int):
    """Fetch a specific user as a discord object."""
    if not _client.guilds:
        raise GuildNotFoundError("No guilds found for the bot.")
    return _client.guilds[0].get_member(user_id)


async def get_user_info(user_id: int) -> Optional[Member]:
    """Get information about a user in the server."""
    member = fetch_user_by_id(user_id)
    if not member:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    return _convert_member(member)


async def send_direct_message(user_id: int, content: str):
    """Send a direct message as a string to a user."""
    member = fetch_user_by_id(user_id)
    if member:
        await member.send(content)
    else:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")


async def send_direct_message_with_embed(user_id: int, content: str, embed: Embed):
    """Send a direct message with an embed to a user."""
    member = fetch_user_by_id(user_id)
    if member:
        d_embed = discord.Embed.from_dict(embed.model_dump())
        await member.send(content, embed=d_embed)
    else:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")


async def change_user_nickname(user_id: int, new_nickname: str):
    """Change the nickname of a user in the server."""
    member = fetch_user_by_id(user_id)
    if member:
        await member.edit(nick=new_nickname)
    else:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
