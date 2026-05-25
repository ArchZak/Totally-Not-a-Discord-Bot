import totally_not_a_bot.internals.dto.roles_dtos as roles_dto
from totally_not_a_bot.config.models import Role

# region Roles Resources


async def get_all_roles() -> list[Role]:
    """
    Get all roles and other associated information about the roles in the server.

    Args:
        None

    Returns:
        list[Role]: A list of Role objects representing the roles in the server
    """
    return await roles_dto.get_all_roles_in_guild()


async def get_role_by_id(role_id: int) -> Role | None:
    """
    Get the information about a role after passing in its id.

    Args:
        role_id (int): The ID of the role to fetch information from

    Returns:
        Role: An object representing the role in the server
    """
    return await roles_dto.get_role_by_id(role_id)


# endregion

# region Roles Tools


def assign_role_to_user(user_id: int, role_id: int):
    """
    Assign a role to a user.

    Args:
        user_id (int): The ID of the user to assign the role to
        role_id (int): The ID of the role to assign the user

    Returns:
        None
    """


def remove_role_from_user(user_id: int, role_id: int):
    """
    Remove a role to a user.

    Args:
        user_id (int): The ID of the user to Remove the role to
        role_id (int): The ID of the role to Remove the user

    Returns:
        None
    """


async def create_role(name: str, permissions: int):
    """
    Create a new role for the server.
    """
    pass


async def edit_role(role_id: int, name: str = None, permissions: int = None):
    """
    Edit a role in the server.
    """
    pass


async def delete_role(role_id: int):
    """
    Delete a new role for the server.

    Args:
        role_id (int): The ID of the role to delete

    Returns:
        None
    """
    await roles_dto.get_role_by_id(role_id).delete()


# endregion
