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
    channel_description: str
    channel_type: str
    # TODO: add perms to channel
