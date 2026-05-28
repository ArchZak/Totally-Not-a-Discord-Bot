from typing import Annotated

from totally_not_a_bot.config.models import Channel
from totally_not_a_bot.internals.services import category_services


async def get_all_categories_info() -> list[Channel]:
    """
    Get all categories and their information in the server.

    Args:
        None

    Returns:
        list[Channel]: A list of Channel objects representing categories
    """
    return await category_services.get_all_categories_info()


async def create_category(
    name: Annotated[str, "The name of the new category"],
    is_private: Annotated[bool, "Whether the category should be hidden from @everyone"] = False,
    allowed_role_ids: Annotated[list[int] | None, "A list of role IDs allowed to view this category"] = None
):
    """
    Create a new category in the server.

    Args:
        name (str): The name of the new category
        is_private (bool): Whether the category should be hidden from @everyone
        allowed_role_ids (list[int] | None): A list of role IDs allowed to view this category

    Returns:
        None
    """
    return await category_services.create_category_service(
        name, is_private, allowed_role_ids
    )


async def edit_category(
    category_id: Annotated[int, "The ID of the category to edit"],
    new_name: Annotated[str | None, "The new name for the category"] = None,
    is_private: Annotated[bool | None, "Whether the category should be hidden from @everyone"] = None,
    allowed_role_ids: Annotated[list[int] | None, "A list of role IDs allowed to view this category"] = None,
):
    """
    Edit the name or permissions of a category in the server.

    Args:
        category_id (int): The ID of the category to edit
        new_name (str | None): The new name for the category
        is_private (bool | None): Whether the category should be hidden from @everyone
        allowed_role_ids (list[int] | None): A list of role IDs allowed to view this category

    Returns:
        None
    """
    return await category_services.edit_category_service(
        category_id, new_name, is_private, allowed_role_ids
    )


async def delete_category(category_id: Annotated[int, "The ID of the category to delete"]):
    """
    Delete a category from the server.

    Args:
        category_id (int): The ID of the category to delete

    Returns:
        None
    """
    return await category_services.delete_category_service(category_id)


async def move_category(
    category_id: Annotated[int, "The ID of the category to move"],
    new_position: Annotated[int, "The new position for the category (0-based index)"]
):
    """
    Move a category to a new position in the server.

    Args:
        category_id (int): The ID of the category to move
        new_position (int): The new position for the category (0-based index)

    Returns:
        None
    """
    return await category_services.move_category_service(category_id, new_position)
