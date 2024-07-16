from pydantic import BaseModel # type: ignore

class Preference(BaseModel):
    id: int
    genre: str