from pydantic import BaseModel

class CreateNote(BaseModel):
    title: str
    text: str

class DeleteNote(BaseModel):
    id: int

class ShowNote(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True