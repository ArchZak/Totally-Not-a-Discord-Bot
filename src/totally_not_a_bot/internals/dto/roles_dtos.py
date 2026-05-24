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

# endregion