from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta
from conf.db_conf import SECRET_KEY, ALGORITHM, EXPIRE_TIME, Oauth2_scheme
from schemas.user import CurrentUser

class TokenScheme(BaseModel):
    token: str


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=EXPIRE_TIME)

    to_encode.update({"exp": expire})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return jwt_token


def get_current_user(token: str = Depends(Oauth2_scheme)) -> CurrentUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="credentials invalid",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        name: str = payload.get("sub")
        user_id: int = payload.get("id")

        print(payload, name, user_id)

        if name is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return CurrentUser(name=name,
                       user_id=user_id)