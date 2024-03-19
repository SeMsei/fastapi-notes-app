from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserScheme, ShowUser
from sqlalchemy.orm import Session
from conf.db_conf import get_db, pwd_context
from models.user import *

signup_router = APIRouter(tags=["Signup"])


@signup_router.post("/Register",
                   status_code=status.HTTP_201_CREATED,
                   response_model=ShowUser)
async def create_user(request: UserScheme, db: Session = Depends(get_db)):
    print(request)
    new_user = User(name=request.name,
                    password=pwd_context.hash(request.password)
                    )

    if db.query(User).filter(User.name == request.name).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="the name {} already exists!".format(request.name)
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user