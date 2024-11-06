from pathlib import Path

from fastapi.security import OAuth2PasswordBearer
from starlette import status
from model.user_request import UserRequest
from fastapi import APIRouter, Depends

from model.user_response import UserResponse
from service import auth_service
from service import user_service
from exceptions.security_exceptions import token_exception

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={401: {"user": "Not authorized"}}
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    await user_service.create_user(user_request)


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(token: str = Depends(oauth2_bearer)):
    user_response = await auth_service.validate_user(token)
    if user_response is None:
        raise token_exception()
    return await user_service.get_user_by_id(user_response.id)
