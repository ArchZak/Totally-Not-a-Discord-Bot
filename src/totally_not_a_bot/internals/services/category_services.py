import totally_not_a_bot.internals.dto.category_dtos as category_dtos
from totally_not_a_bot.config.models import Channel

# region Category Tools


async def get_all_categories_info() -> list[Channel]:
    """
    Get all categories and their information in the server.

    Args:
        None

    Returns:
        list[Channel]: A list of Channel objects representing categories
    """
    return await category_dtos.get_all_categories_info()


async def create_category(
    name: str, is_private: bool = False, allowed_role_ids: list[int] | None = None
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
    await category_dtos.create_category(name, is_private, allowed_role_ids)


async def edit_category(
    category_id: int,
    new_name: str | None = None,
    is_private: bool | None = None,
    allowed_role_ids: list[int] | None = None,
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
    await category_dtos.edit_category(
        category_id, new_name, is_private, allowed_role_ids
    )


async def delete_category(category_id: int):
    """
    Delete a category from the server.

    Args:
        category_id (int): The ID of the category to delete

    Returns:
        None
    """
    await category_dtos.delete_category(category_id)


async def move_category(category_id: int, new_position: int):
    """
    Move a category to a new position in the server.

    Args:
        category_id (int): The ID of the category to move
        new_position (int): The new position for the category

    Returns:
        None
    """
    await category_dtos.move_category(category_id, new_position)


# endregion
