from typing import Optional

import totally_not_a_bot.internals.dto.users_dtos as users_dtos
from totally_not_a_bot.config.models import Embed, Member

# region User Tools


async def get_user_info_service(user_id: int) -> Optional[Member]:
    """
    Get information about a user in the server, such as their username, roles, and join date.

    Args:
        user_id (int): The ID of the user to fetch information from

    Returns:
        Optional[Member]: A Member object containing the user's information
    """
    return await users_dtos.get_user_info(user_id)


async def send_direct_message_service(user_id: int, content: str):
    """
    Send a direct message to a user.

    Args:
        user_id (int): The ID of the user to send the message to
        content (str): The content of the message to send

    Returns:
        None
    """
    await users_dtos.send_direct_message(user_id, content)


async def send_direct_message_with_embed_service(
    user_id: int, content: str, embed: Embed
):
    """
    Send a direct message with an embed to a user.

    Args:
        user_id (int): The ID of the user to send the message to
        content (str): The content of the message to send
        embed (Embed): The embed to include in the message

    Returns:
        None
    """
    await users_dtos.send_direct_message_with_embed(user_id, content, embed)


async def change_user_nickname_service(user_id: int, new_nickname: str):
    """
    Change the nickname of a user in the server.

    Args:
        user_id (int): The ID of the user to change the nickname for
        new_nickname (str): The new nickname to set for the user

    Returns:
        None
    """
    await users_dtos.change_user_nickname(user_id, new_nickname)


# endregion
