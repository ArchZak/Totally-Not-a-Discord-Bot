from typing import Optional

import discord

import totally_not_a_bot.internals.dto.users_dtos as users_dtos
from totally_not_a_bot.config.app import _client
from totally_not_a_bot.config.exceptions import GuildNotFoundError, MemberNotFoundError
from totally_not_a_bot.config.models import User


async def get_user_info_service(user_id: int) -> Optional[User]:
    guild = _client.get_guild(_client.target_guild_id)
    if not guild:
        raise GuildNotFoundError("Target guild not found or bot is not in it.")

    member = guild.get_member(user_id)
    if not member:
        try:
            member = await guild.fetch_member(user_id)
        except discord.NotFound:
            pass

    if member:
        return users_dtos._convert_user(member)

    # Fallback to user if not in guild
    try:
        user = await _client.fetch_user(user_id)
        return users_dtos._convert_user(user)
    except discord.NotFound:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")


async def send_direct_message_service(user_id: int, message: str) -> Optional[int]:
    try:
        user = await _client.fetch_user(user_id)
        if not user.dm_channel:
            await user.create_dm()
        sent_message = await user.dm_channel.send(message)
        return sent_message.id
    except discord.NotFound:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    except discord.Forbidden:
        # Cannot send DM
        return None


async def send_direct_message_with_embed_service(
    user_id: int, title: str, description: str, color: int = 0x00FF00
) -> Optional[int]:
    try:
        user = await _client.fetch_user(user_id)
        if not user.dm_channel:
            await user.create_dm()

        embed = discord.Embed(title=title, description=description, color=color)
        sent_message = await user.dm_channel.send(embed=embed)
        return sent_message.id
    except discord.NotFound:
        raise MemberNotFoundError(f"User with ID {user_id} not found.")
    except discord.Forbidden:
        return None
