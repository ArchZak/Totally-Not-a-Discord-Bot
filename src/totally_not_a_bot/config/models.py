from datetime import datetime
from typing import Optional, Union

from discord import Colour
from pydantic import BaseModel


class Message(BaseModel):
    content: str
    author_id: int
    channel_id: int
    timestamp: str


class Role(BaseModel):
    name: str
    role_id: int
    # TODO: add intents and update descriptions


class Channel(BaseModel):
    name: str
    channel_id: int
    channel_description: Optional[str]
    channel_type: str
    # TODO: add perms to channel


class Embed(BaseModel):
    title: Optional[str]
    type: str = "rich"
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[datetime.datetime]
    color: Optional[Union[Colour, int]]
