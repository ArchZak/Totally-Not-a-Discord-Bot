import pytest
from unittest.mock import AsyncMock

import totally_not_a_bot.tools.messages_tools as messages_tools


@pytest.mark.asyncio
async def test_send_message_calls_service(monkeypatch):
    fake = type("Svc", (), {})()
    fake.send_message_service = AsyncMock(return_value={"id": 123, "content": "hello"})
    monkeypatch.setattr(messages_tools, "messages_services", fake)

    result = await messages_tools.send_message(42, "hello", reply_to_message_id=99)

    fake.send_message_service.assert_awaited_once_with(42, "hello", 99)
    assert result == {"id": 123, "content": "hello"}


@pytest.mark.asyncio
async def test_send_message_default_reply_none(monkeypatch):
    fake = type("Svc", (), {})()
    fake.send_message_service = AsyncMock(return_value={"id": 124})
    monkeypatch.setattr(messages_tools, "messages_services", fake)

    result = await messages_tools.send_message(7, "no reply")

    fake.send_message_service.assert_awaited_once_with(7, "no reply", None)
    assert result == {"id": 124}
