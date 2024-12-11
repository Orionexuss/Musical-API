from pydantic import BaseModel

class MoodRequest(BaseModel):
    text: str