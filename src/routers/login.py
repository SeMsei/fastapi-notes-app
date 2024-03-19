from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from conf.db_conf import get_db, pwd_context, Oauth2_scheme
from models.user import *
from schemas.token import create_access_token
from schemas.user import UserScheme

login_router = APIRouter(tags=["Signup"])


@login_router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(request: UserScheme, db: Session = Depends(get_db)):
    print(request)
    login_user = db.query(User).filter(request.name == User.name).first()
    
    if not login_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="{} does not exist".format(request.name)
                            )
    if not pwd_context.verify(request.password, login_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="incorrect password"
                            )
    token = create_access_token(data={"sub": login_user.name,
                                      "id": login_user.user_id
                                      })

    return {"access_token": token, "token_type": "bearer"}

