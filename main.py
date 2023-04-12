from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from entities import User, Session
from dtos.request import UserReqModel

from controllers.user_controller import include_route as usuario_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:300"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

usuario_controller(app)