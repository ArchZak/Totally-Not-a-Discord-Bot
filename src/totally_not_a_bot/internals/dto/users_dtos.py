import discord

from totally_not_a_bot.config.models import User


def _convert_user(user: discord.Member | discord.User) -> User:
    member_details = None
    if isinstance(user, discord.Member):
        member_details = {
            "nickname": user.nick,
            "roles": [role.id for role in user.roles],
            "joined_at": user.joined_at,
            "is_timed_out": user.is_timed_out(),
        }

    return User(
        user_id=user.id,
        username=user.name,
        discriminator=user.discriminator,
        is_bot=user.bot,
        member_details=member_details,
    )
