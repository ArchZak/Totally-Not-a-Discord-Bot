from typing import Annotated, Literal

from dto import profiles_dto

# region Profile Tools


async def set_user_status(status: str):
    """
    Set the status of the discord bot.

    Args:
        status (str): The new status for the bot user

    Returns:
        None
    """
    await profiles_dto.set_user_status_dto(status)


async def set_user_activity(
    activity_type: Annotated[
        str,
        Literal["playing", "streaming", "listening", "watching"],
        'The type of activity (e.g., "playing", "streaming", "listening", "watching")',
    ],
    activity_name: str,
):
    """
    Set the activity of the discord bot.

    Args:
        activity_type (str): The type of activity (e.g., "playing", "streaming", "listening", "watching")
        activity_name (str): The name of the activity

    Returns:
        None
    """
    await profiles_dto.set_user_activity_dto(activity_type, activity_name)


# endregion
