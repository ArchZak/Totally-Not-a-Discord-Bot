import totally_not_a_bot.internals.dto.category_dtos as category_dtos
from totally_not_a_bot.config.models import Category

# region Category Tools


async def get_all_categories_info_service() -> list[Category]:
    """
    Get all categories and their information in the server.

    Args:
        None

    Returns:
        list[Category]: A list of Category objects representing categories
    """
    return await category_dtos.get_all_categories_info()


async def create_category_service(
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
    return await category_dtos.create_category(name, is_private, allowed_role_ids)


async def create_category_with_channels_service(
    name: str,
    channels: list[dict],
    is_private: bool = False,
    allowed_role_ids: list[int] | None = None,
):
    """
    Create a new category in the server along with specified channels within it.

    Args:
        name (str): The name of the new category
        channels (list[dict]): A list of dictionaries representing channels to create within the category, each with a 'name' and 'type' (e.g., 'text', 'voice', 'forum')
        is_private (bool): Whether the category should be hidden from @everyone
        allowed_role_ids (list[int] | None): A list of role IDs allowed to view this category

    Returns:
        None
    """


async def edit_category_service(
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


async def delete_category_service(category_id: int):
    """
    Delete a category from the server.

    Args:
        category_id (int): The ID of the category to delete

    Returns:
        None
    """
    await category_dtos.delete_category(category_id)


async def move_category_service(category_id: int, new_position: int):
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
