from fastapi import APIRouter, Depends, HTTPException, status, Response
from schemas.note import CreateNote, DeleteNote
from schemas.token import TokenScheme
from sqlalchemy.orm import Session
from conf.db_conf import get_db
from models.user import *
from models.note import *
from schemas.token import get_current_user
from schemas.user import CurrentUser

note_router = APIRouter(tags=["note"])

@note_router.put("/notes/{note_id}", status_code=status.HTTP_200_OK)
def update_notes(note_id: int, request: CreateNote, response: Response, db: Session = Depends(get_db),
                currente_user: CurrentUser = Depends(get_current_user)):
    notes = db.query(Note).filter(Note.note_id == note_id).all()

    if len(notes) < 1:
        response.status_code = status.HTTP_404_NOT_FOUND 
        return {"message": "There's no such note"}

    db.query(Note).filter(Note.note_id == note_id).update(dict(note_id=note_id, user_id=currente_user.user_id, title = request.title, text=request.text))
    db.commit()
    note = db.query(Note).filter(Note.note_id == note_id).first()
    return note

@note_router.delete("/notes/{note_id}", status_code=status.HTTP_200_OK)
def delete_notes(note_id: int, response: Response, db: Session = Depends(get_db),
                currente_user: CurrentUser = Depends(get_current_user)):
    notes = db.query(Note).filter(Note.note_id == note_id).all()

    if len(notes) < 1:
        response.status_code = status.HTTP_404_NOT_FOUND 
        return {"message": "There's no such note"}

    db.query(Note).filter(Note.note_id == note_id).delete()
    db.commit()
    response.status_code = status.HTTP_202_ACCEPTED 
    return {"message": "Item deleted"}

@note_router.get("/notes", status_code=status.HTTP_200_OK)
def get_notes(db: Session = Depends(get_db),
                currente_user: CurrentUser = Depends(get_current_user)):
    notes = db.query(Note).filter(Note.user_id == currente_user.user_id).all()
    return notes

@note_router.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(request: CreateNote, db: Session = Depends(get_db),
                currente_user: CurrentUser = Depends(get_current_user)
                ):
    me = db.query(User).filter(User.name == currente_user.name).first()
    
    note = Note(
        title=request.title,
        text=request.text,
        user_id=me.user_id
    )
    db.add(note)
    db.commit()
    db.refresh(note)

    return note