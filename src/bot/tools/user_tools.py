from typing import Annotated

from bot.internals.services import users_services
from bot.models import Embed


async def get_user_info(
    user_id: Annotated[int, "The ID of the user to fetch information from"],
):
    """
    Get information about a user in the server, such as their username, roles, and join date.

    Args:
        user_id (int): The ID of the user to fetch information from

    Returns:
        Optional[Member]: A Member object containing the user's information
    """
    return await users_services.get_user_info_service(user_id)


async def send_direct_message(
    user_id: Annotated[int, "The ID of the user to send the message to"],
    content: Annotated[str, "The content of the message to send"],
):
    """
    Send a direct message to a user.

    Args:
        user_id (int): The ID of the user to send the message to
        content (str): The content of the message to send

    Returns:
        None
    """
    return await users_services.send_direct_message_service(user_id, content)


async def send_direct_message_with_embed(
    user_id: Annotated[int, "The ID of the user to send the message to"],
    content: Annotated[str, "The content of the message to send"],
    embed: Annotated[Embed, "The embed to include in the message"],
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
    return await users_services.send_direct_message_with_embed_service(
        user_id, content, embed
    )
