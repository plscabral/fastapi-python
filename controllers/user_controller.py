from fastapi import FastAPI, APIRouter

from dtos.request import UserReqModel
from entities import User, Session

router = APIRouter(prefix='/users', tags=["Usuários"])


@router.get("")
def get_users():
    session = Session()
    users = session.query(User).all()
    return users


@router.get("/{id}")
def get_users_by_id(id: int):
    session = Session()
    user = session.query(User).filter(User.id == id).first()
    return user


@router.post("")
def create_user(model: UserReqModel):
    user = User(name=model.name, email=model.email, password=model.password)
    session = Session()
    session.add(user)
    session.commit()
    return {"success": True, "message": "Usuário criado com sucesso!"}


def include_route(app: FastAPI):
    app.include_router(router)
