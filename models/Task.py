from pydantic import BaseModel, Field
from datetime import datetime

class Task(BaseModel):
    date: datetime
    title: str = Field(max_length=140)
    description: str
    priority: bool | None = None
