from langchain.agents import create_agent
from langchain_core.tools import StructuredTool

from bot.tools.category_tools import (
    bulk_create_categories,
    bulk_delete_categories,
    bulk_edit_categories,
    create_category,
    delete_category,
    edit_category,
    get_all_categories_info,
    move_category,
)
from bot.tools.channels_tools import (
    bulk_create_channels,
    bulk_delete_channels,
    bulk_edit_channels,
    create_channel,
    delete_channel,
    edit_channel,
    get_all_channels_info,
    get_channel_info,
    move_channel,
    set_channel_position,
)
from bot.tools.enforcement_tools import (
    ban_user,
    disconnect_user,
    kick_user,
    move_user,
    mute_user,
    unban_user,
    unmute_user,
)
from bot.tools.messages_tools import (
    add_reaction,
    delete_message,
    edit_embed,
    edit_message,
    get_pinned_messages,
    get_recent_messages,
    get_thread_from_message,
    pin_message,
    remove_reaction,
    send_embed,
    send_message,
    unpin_message,
)
from bot.tools.profile_tools import set_bot_activity, set_bot_status
from bot.tools.role_tools import (
    assign_role_to_user,
    create_role,
    delete_role,
    edit_role,
    get_all_roles,
    get_role_by_id,
    remove_role_from_user,
)
from bot.tools.user_tools import (
    get_user_info,
    send_direct_message,
    send_direct_message_with_embed,
)


async def build_native_agent():
    tool_funcs = [
        get_all_categories_info,
        bulk_create_categories,
        bulk_edit_categories,
        bulk_delete_categories,
        create_category,
        edit_category,
        delete_category,
        move_category,
        get_channel_info,
        get_all_channels_info,
        bulk_create_channels,
        bulk_edit_channels,
        bulk_delete_channels,
        create_channel,
        edit_channel,
        delete_channel,
        move_channel,
        set_channel_position,
        get_recent_messages,
        get_pinned_messages,
        get_thread_from_message,
        send_message,
        edit_message,
        delete_message,
        send_embed,
        edit_embed,
        pin_message,
        unpin_message,
        add_reaction,
        remove_reaction,
        set_bot_status,
        set_bot_activity,
        get_all_roles,
        get_role_by_id,
        assign_role_to_user,
        remove_role_from_user,
        create_role,
        edit_role,
        delete_role,
        get_user_info,
        send_direct_message,
        send_direct_message_with_embed,
        mute_user,
        unmute_user,
        kick_user,
        ban_user,
        unban_user,
        move_user,
        disconnect_user,
    ]

    tools = [StructuredTool.from_function(coroutine=tool) for tool in tool_funcs]

    agent = create_agent(
        "model-name-here",
        tools,
        system_prompt=(
            "You're a Discord moderator, enforce the rules and keep things running smoothly."
        ),
    )
    return agent
