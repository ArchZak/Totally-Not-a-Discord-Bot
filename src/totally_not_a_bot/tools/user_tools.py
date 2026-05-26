from totally_not_a_bot.config.models import Embed
from totally_not_a_bot.server import mcp


@mcp.tool(
    "get_user_info",
    "Get information about a user in the server, such as their username, roles, and join date.",
)
async def get_user_info(user_id: int):
    """
    Get information about a user in the server, such as their username, roles, and join date.

    Args:
        user_id (int): The ID of the user to fetch information from

    Returns:
        Optional[Member]: A Member object containing the user's information
    """


@mcp.tool("send_direct_message", "Send a direct message to a user.")
async def send_direct_message(user_id: int, content: str):
    """
    Send a direct message to a user.

    Args:
        user_id (int): The ID of the user to send the message to
        content (str): The content of the message to send

    Returns:
        None
    """


@mcp.tool(
    "send_direct_message_with_embed", "Send a direct message with an embed to a user."
)
async def send_direct_message_with_embed(user_id: int, content: str, embed: Embed):
    """
    Send a direct message with an embed to a user.

    Args:
        user_id (int): The ID of the user to send the message to
        content (str): The content of the message to send
        embed (Embed): The embed to include in the message

    Returns:
        None
    """
