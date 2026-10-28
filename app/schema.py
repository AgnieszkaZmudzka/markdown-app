from pydantic import BaseModel, Field

class Note(BaseModel):
    filename: str = Field(),
    content: str


