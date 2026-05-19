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
