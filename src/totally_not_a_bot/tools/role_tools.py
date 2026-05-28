from typing_extensions import Annotated

from totally_not_a_bot.config.models import Role
from totally_not_a_bot.internals.services import roles_services


async def get_all_roles() -> list[Role]:
    """
    Get all roles and other associated information about the roles in the server.

    Args:
        None

    Returns:
        list[Role]: A list of Role objects representing the roles in the server
    """
    return await roles_services.get_all_roles_service()


async def get_role_by_id(
    role_id: Annotated[int, "The ID of the role to fetch information from"],
) -> Role | None:
    """
    Get the information about a role after passing in its id.

    Args:
        role_id (int): The ID of the role to fetch information from

    Returns:
        Role: An object representing the role in the server
    """
    return await roles_services.get_role_by_id_service(role_id)


async def assign_role_to_user(
    user_id: Annotated[int, "The ID of the user to assign the role to"],
    role_id: Annotated[int, "The ID of the role to assign the user"],
) -> None:
    """
    Assign a role to a user.

    Args:
        user_id (int): The ID of the user to assign the role to
        role_id (int): The ID of the role to assign the user

    Returns:
        None
    """
    return await roles_services.assign_role_to_user_service(user_id, role_id)


async def remove_role_from_user(
    user_id: Annotated[int, "The ID of the user to remove the role from"],
    role_id: Annotated[int, "The ID of the role to remove from the user"],
) -> None:
    """
    Remove a role from a user.

    Args:
        user_id (int): The ID of the user to remove the role from
        role_id (int): The ID of the role to remove from the user

    Returns:
        None
    """
    return await roles_services.remove_role_from_user_service(user_id, role_id)


async def create_role(
    name: Annotated[str, "The name of the role to create"],
    permissions: Annotated[
        int | None,
        "The permissions to assign to the role, represented as a bitwise integer. If None, the role will have no permissions",
    ] = None,
    color: Annotated[
        int | None,
        "The color to assign to the role, represented as an integer. If None, the role will have no color",
    ] = None,
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
    return await roles_services.create_role_service(name, permissions, color)


async def edit_role(
    role_id: Annotated[int, "The ID of the role to edit"],
    name: Annotated[
        str | None,
        "The new name of the role. If None, the role's name will not be changed.",
    ] = None,
    permissions: Annotated[
        int | None,
        "The new permissions to assign to the role, represented as a bitwise integer. If None, the role's permissions will not be changed.",
    ] = None,
    color: Annotated[
        int | None,
        "The new color to assign to the role, represented as an integer. If None, the role's color will not be changed.",
    ] = None,
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
    return await roles_services.edit_role_service(role_id, name, permissions, color)


async def delete_role(role_id: Annotated[int, "The ID of the role to delete"]):
    """
    Delete a new role for the server.

    Args:
        role_id (int): The ID of the role to delete

    Returns:
        None
    """
    return await roles_services.delete_role_service(role_id)
