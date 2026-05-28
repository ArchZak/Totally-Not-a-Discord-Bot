from typing import Annotated

from totally_not_a_bot.config.models import (
    Category,
    CategoryParam,
    Channel,
    ChannelParam,
)
from totally_not_a_bot.internals.services import category_services


async def get_category_info(
    category_id: Annotated[int, "The ID of the category to fetch information from"],
) -> Category:
    """
    Get the information about a category after passing in its id.

    Args:
        category_id (int): The ID of the category to fetch information from

    Returns:
        Channel: An object representing the category in the server
    """
    return await category_services.get_category_info(category_id)


async def get_all_categories_info() -> list[Category]:
    """
    Get all the categories in the server and their information.

    Args:
        None

    Returns:
        list[Category]: A list of Category objects representing categories
    """
    return await category_services.get_all_categories_info_service()


async def create_category(
    name: Annotated[str, "The name of the new category"],
    is_private: Annotated[
        bool, "Whether the category should be hidden from @everyone"
    ] = False,
    allowed_role_ids: Annotated[
        list[int] | None, "A list of all the role IDs allowed to view this category"
    ] = None,
) -> int:
    """
    Create a new category in the server.

    Args:
        name (str): The name of the new category
        is_private (bool): Whether the category should be hidden from @everyone
        allowed_role_ids (list[int] | None): A list of all the role IDs allowed to view this category

    Returns:
        category_id (int): The id of the category that was made
    """
    return await category_services.create_category_service(
        name, is_private, allowed_role_ids
    )


async def bulk_create_categories(
    categories: Annotated[
        list[CategoryParam],
        "A list of dictionaries representing categories to create, each with a 'name', 'is_private' boolean, and 'allowed_role_ids' list of ints",
    ],
) -> list[int]:
    """
    Create multiple categories in the server at once.

    Args:
        categories (list[CategoryParam]): A list of CategoryParam objects representing categories to create, each with a 'name', 'is_private' boolean, and 'allowed_role_ids' list of ints

    Returns:
        list[int]: A list of IDs for the categories that were made
    """
    category_ids = []
    for category in categories:
        category_id = await category_services.create_category_service(
            name=category.name,
            is_private=category.is_private,
            allowed_role_ids=category.allowed_role_ids,
        )
        category_ids.append(category_id)
    return category_ids


async def create_category_with_channels(
    name: Annotated[str, "The name of the new category"],
    channels: Annotated[
        list[ChannelParam],
        "A list of dictionaries representing channels to create within the category, each with a 'name' and 'type' (e.g., 'text', 'voice', 'forum')",
    ],
    is_private: Annotated[
        bool, "Whether the category should be hidden from @everyone"
    ] = False,
    allowed_role_ids: Annotated[
        list[int] | None, "A list of all the role IDs allowed to view this category"
    ] = None,
) -> int:
    """
    Create a new category in the server along with specified channels within it. The channels will automatically inherit the same permissions as the category.

    Args:
        name (str): The name of the new category
        channels (list[ChannelParam]): A list of ChannelParam objects representing channels to create within the category, each with a 'name' and 'type' (e.g., 'text', 'voice', 'forum')
        is_private (bool): Whether the category should be hidden from @everyone
        allowed_role_ids (list[int] | None): A list of all the role IDs allowed to view this category

    Returns:
        category_id (int): The id of the category that was made
    """
    return await category_services.create_category_with_channels_service(
        name, channels, is_private, allowed_role_ids
    )


async def edit_category(
    category_id: Annotated[int, "The ID of the category to edit"],
    new_name: Annotated[str | None, "The new name for the category"] = None,
    is_private: Annotated[
        bool | None, "Whether the category should be hidden from @everyone"
    ] = None,
    allowed_role_ids: Annotated[
        list[int] | None, "A list of role IDs allowed to view this category"
    ] = None,
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


async def bulk_edit_categories(
    categories: Annotated[
        list[Category],
        "A list of Category objects representing categories to edit, each with an 'id' and optional 'name', 'is_private' boolean, and 'allowed_role_ids' list",
    ],
):
    """
    Edit the name or permissions of multiple categories in the server.

    Args:
        categories (list[Category]): A list of Category objects representing categories to edit, each with an 'id' and optional 'name', 'is_private' boolean, and 'allowed_role_ids' list

    Returns:
        list[int]: A list of IDs for the categories that were edited
    """
    for category in categories:
        await category_services.edit_category_service(
            category_id=category.category_id,
            new_name=category.name,
            is_private=category.is_private,
            allowed_role_ids=category.allowed_role_ids,
        )


async def delete_category(
    category_id: Annotated[int, "The ID of the category to delete"],
):
    """
    Delete a category from the server.

    Args:
        category_id (int): The ID of the category to delete

    Returns:
        None
    """
    return await category_services.delete_category_service(category_id)


async def bulk_delete_categories(
    category_ids: Annotated[list[int], "A list of IDs for the categories to delete"],
):
    """
    Delete multiple categories from the server.

    Args:
        category_ids (list[int]): A list of IDs for the categories to delete

    Returns:
        list[int]: A list of IDs for the categories that were deleted
    """
    for category_id in category_ids:
        await category_services.delete_category_service(category_id)


async def move_category(
    category_id: Annotated[int, "The ID of the category to move"],
    new_position: Annotated[int, "The new position for the category (0-based index)"],
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
