from config.models import Role

# region Roles Resources


def get_all_roles() -> list[Role]:
    """
    Get all roles and other associated information about the roles in the server.

    Args:
        None

    Returns:
        list[Role]: A list of Role objects representing the roles in the server
    """
    pass


def get_role_by_id(role_id: int) -> Role:
    """
    Get the information about a role after passing in its id.

    Args:
        role_id (int): The ID of the role to fetch information from

    Returns:
        Role: An object representing the role in the server
    """


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


def create_role(name: str, permissions: int):
    """
    Create a new role for the server.
    """


def edit_role(role_id: int, name: str = None, permissions: int = None):
    """
    Edit a role in the server.
    """


def delete_role(role_id: int):
    """
    Delete a new role for the server.
    """


def bulk_assign_role_to_users(user_ids: list[int], role_id: int): #make bulk versions a decision layer action
    pass


# endregion
