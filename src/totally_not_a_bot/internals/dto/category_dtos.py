import discord

from totally_not_a_bot.config.models import Category


def _convert_category(category: discord.CategoryChannel) -> Category:
    return Category(
        name=category.name,
        category_id=category.id,
        is_private=category.is_private(),
        allowed_role_ids=[
            role.id for role in category.overwrites if isinstance(role, discord.Role)
        ],
    )
