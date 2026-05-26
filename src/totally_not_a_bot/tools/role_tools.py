from totally_not_a_bot.config.models import Role
from totally_not_a_bot.server import mcp


@mcp.tool("get_all_roles")
async def get_all_roles() -> list[Role]:
    """
    Get all roles and other associated information about the roles in the server.

    Args:
        None

    Returns:
        list[Role]: A list of Role objects representing the roles in the server
    """


@mcp.tool("get_role_by_id")
async def get_role_by_id(role_id: int) -> Role | None:
    """
    Get the information about a role after passing in its id.

    Args:
        role_id (int): The ID of the role to fetch information from

    Returns:
        Role: An object representing the role in the server
    """


@mcp.tool("assign_role_to_user")
async def assign_role_to_user(user_id: int, role_id: int):
    """
    Assign a role to a user.

    Args:
        user_id (int): The ID of the user to assign the role to
        role_id (int): The ID of the role to assign the user

    Returns:
        None
    """


@mcp.tool("remove_role_from_user")
async def remove_role_from_user(user_id: int, role_id: int):
    """
    Remove a role from a user.

    Args:
        user_id (int): The ID of the user to Remove the role to
        role_id (int): The ID of the role to Remove the user

    Returns:
        None
    """


@mcp.tool("create_role")
async def create_role(
    name: str, permissions: int | None = None, color: int | None = None
):
    """
    Create a new role for the server.

    Args:
        name (str): The name of the role to create
        permissions (int | None): The permissions to assign to the role, represented as a bitwise integer. If None, the role will have no permissions.
        color (int | None): The color to assign to the role, represented as an integer. If None, the role will have no color.

    Returns:
        None
    """


@mcp.tool("edit_role")
async def edit_role(
    role_id: int,
    name: str | None = None,
    permissions: int | None = None,
    color: int | None = None,
):
    """
    Edit an existing role for the server.

    Args:
        role_id (int): The ID of the role to edit
        name (str | None): The new name of the role. If None, the role's name will not be changed.
        permissions (int | None): The new permissions to assign to the role, represented as a bitwise integer. If None, the role's permissions will not be changed.
        color (int | None): The new color to assign to the role, represented as an integer. If None, the role's color will not be changed.

    Returns:
        None
    """


@mcp.tool("delete_role")
async def delete_role(role_id: int):
    """
    Delete a new role for the server.

    Args:
        role_id (int): The ID of the role to delete

    Returns:
        None
    """
