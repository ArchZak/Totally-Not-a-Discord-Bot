from unittest.mock import AsyncMock, patch

import pytest

from totally_not_a_bot.internals.services.profile_services import set_bot_status_service


@pytest.mark.asyncio
async def test_set_bot_status_service():
    with patch("totally_not_a_bot.config.app._client") as mock_client:
        mock_client.change_presence = AsyncMock()

        await set_bot_status_service("online")

        mock_client.change_presence.assert_called_once_with(status="online")


@pytest.mark.asyncio
async def test_set_bot_status_service_different_statuses():
    statuses = ["online", "idle", "dnd", "invisible"]

    for status in statuses:
        with patch("totally_not_a_bot.config.app._client") as mock_client:
            mock_client.change_presence = AsyncMock()

            await set_bot_status_service(status)

            mock_client.change_presence.assert_called_once_with(status=status)
