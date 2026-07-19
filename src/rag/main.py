from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

async def build_agent():
    client = MultiServerMCPClient(
        {
            "discord": {
                "transport": "stdio",
                "command": "python",
                "args": ["/abs/path/to/totally-not-a-bot/src/mcp/server.py"], #needs abs path according to langchain docs
            },
        }
    )

    mcp_tools = await client.get_tools()
    tools = mcp_tools

    agent = create_agent(
        "model-name-here",
        tools,
        system_prompt=(
            "You're a Discord moderator. Enforce the rules and keep things running smoothly."
        ),
    )
    return agent
