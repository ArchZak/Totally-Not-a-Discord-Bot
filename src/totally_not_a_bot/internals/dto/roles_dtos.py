from server import _client
from totally_not_a_bot.config.models import Role

# region Roles Tools

async def get_all_roles_in_guild():
    """
    Get all roles and other associated information about the roles in the server.

    Args:
        None

    Returns:
        list[Role]: A list of Role objects representing the roles in the server
    """
    return _client.guilds[0].roles

async def get_role_by_id(role_id: int) -> Role:
    """
    Get the information about a role after passing in its id.

    Args:
        role_id (int): The ID of the role to fetch information from

    Returns:
        Role: An object representing the role in the server
    """
    return _client.guilds[0].get_role(role_id)

# endregion