from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    content: str
    author_id: int
    channel_id: int
    timestamp: datetime


class Role(BaseModel):
    name: str
    role_id: int
    hoist: bool
    position: int
    mentionable: bool
    color: Optional[int]
    secondary_color: Optional[int] = None
    tertiary_color: Optional[int] = None


class Channel(BaseModel):
    name: str
    channel_id: int
    channel_description: Optional[str] = None
    channel_type: str
    # TODO: add perms to channel


class Embed(BaseModel):
    title: Optional[str] = None
    type: str = "rich"
    description: Optional[str] = None
    url: Optional[str] = None
    timestamp: Optional[datetime] = None
    color: Optional[int] = None


class Member(BaseModel):
    user_id: int
    nickname: Optional[str] = None
    roles: list[int]
