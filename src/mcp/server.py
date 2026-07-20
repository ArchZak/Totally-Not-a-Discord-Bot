import argparse
import asyncio
import os
import sys

from dotenv import load_dotenv
from loguru import logger

from bot.app import _client, mcp
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

# Category tools

mcp.add_tool(get_all_categories_info)
mcp.add_tool(bulk_create_categories)
mcp.add_tool(bulk_edit_categories)
mcp.add_tool(bulk_delete_categories)
mcp.add_tool(create_category)
mcp.add_tool(edit_category)
mcp.add_tool(delete_category)
mcp.add_tool(move_category)

# Channel tools

mcp.add_tool(get_channel_info)
mcp.add_tool(get_all_channels_info)
mcp.add_tool(bulk_create_channels)
mcp.add_tool(bulk_edit_channels)
mcp.add_tool(bulk_delete_channels)
mcp.add_tool(create_channel)
mcp.add_tool(edit_channel)
mcp.add_tool(delete_channel)
mcp.add_tool(move_channel)
mcp.add_tool(set_channel_position)

# Message tools

mcp.add_tool(get_recent_messages)
mcp.add_tool(get_pinned_messages)
mcp.add_tool(get_thread_from_message)
mcp.add_tool(send_message)
mcp.add_tool(edit_message)
mcp.add_tool(delete_message)
mcp.add_tool(send_embed)
mcp.add_tool(edit_embed)
mcp.add_tool(pin_message)
mcp.add_tool(unpin_message)
mcp.add_tool(add_reaction)
mcp.add_tool(remove_reaction)

# Profile tools

mcp.add_tool(set_bot_status)
mcp.add_tool(set_bot_activity)

# Role tools

mcp.add_tool(get_all_roles)
mcp.add_tool(get_role_by_id)
mcp.add_tool(assign_role_to_user)
mcp.add_tool(remove_role_from_user)
mcp.add_tool(create_role)
mcp.add_tool(edit_role)
mcp.add_tool(delete_role)

# User tools

mcp.add_tool(get_user_info)
mcp.add_tool(send_direct_message)
mcp.add_tool(send_direct_message_with_embed)

# Enforcement tools

mcp.add_tool(mute_user)
mcp.add_tool(unmute_user)
mcp.add_tool(kick_user)
mcp.add_tool(ban_user)
mcp.add_tool(unban_user)
mcp.add_tool(move_user)
mcp.add_tool(disconnect_user)

# Redirect loguru to stderr to avoid breaking MCP stdio transport
logger.remove()
logger.add(sys.stderr, level="INFO")


async def main():
    parser = argparse.ArgumentParser(description="Run Totally-Not-A-Bot")
    parser.add_argument(
        "--no-agent",
        action="store_true",
        help="Disable the native autonomous agent loop",
    )
    parser.add_argument(
        "--no-mcp", action="store_true", help="Disable the FastMCP stdio server"
    )
    args = parser.parse_args()

    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")

    if not token:
        logger.error("Missing DISCORD_BOT_TOKEN in .env")
        return

    if args.no_agent:
        _client.enable_agent = False
        logger.info("Native agent loop is disabled")

    # Spin up discord bot on nonblocking thread using start
    asyncio.create_task(_client.start(token))
    logger.info("Spinning up Discord Bot")

    try:
        if not args.no_mcp:
            # Run MCP server on main thread over stdio
            logger.info("MCP Server starting over stdio")
            await mcp.run_async(transport="stdio")
        else:
            logger.info("Running native agent loop")
            while True:
                await asyncio.sleep(3600)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        # Gracefully shutdown the bot
        await _client.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
