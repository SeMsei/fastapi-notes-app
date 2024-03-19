import uvicorn
from fastapi import FastAPI
from conf.db_conf import *
from routers import login, note, register, user
from models.note import *
from models.user import *

Base.metadata.create_all(engine)

app = FastAPI(
    title="FastApiNotes"
)

app.include_router(register.signup_router)
app.include_router(login.login_router)
app.include_router(note.note_router)


@app.get(path="/")
def index():
    return {"detail": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.0", port=8000)