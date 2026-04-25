from fastapi import APIRouter, status, HTTPException, Depends
from shemas.users import User, CreateUser
from shemas.posts import Post

from domain.use_case.user.get_user_by_login import GetUserByLoginUseCase
from domain.use_case.user.create_user import CreateUserUseCase
from domain.use_case.user.delete_user import DeleteUserUseCase

from domain.use_case.post.get_post_by_id import GetPostByIdUseCase
from domain.use_case.post.create_post import CreatePostUseCase
from domain.use_case.post.delete_post import DeletePostUseCase
from domain.use_case.post.change_post import ChangePostUseCase
from api.depends import (
    get_user_by_login_use_case,
    create_user_use_case,
    delete_user_use_case,
    get_post_by_id_use_case,
    create_post_use_case,
    change_post_use_case,
    delete_post_use_case,
)

from core.exceptions.domain_exceptions import *

router = APIRouter()

@router.get("/user/{login}", status_code=status.HTTP_200_OK, response_model=User)
async def get_user_by_login(
    login: str,
    use_case: GetUserByLoginUseCase = Depends(get_user_by_login_use_case),
) -> User:
    try:
        return await use_case.execute(login=login)
    except UserNotFoundByLoginException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.get_detail()
        )

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(
    user: CreateUser,
    use_case: CreateUserUseCase = Depends(create_user_use_case),
) -> User:
    try:
        return await use_case.execute(user=user)
    except UserLoginIsNotUniqueException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exc.get_detail()
        )

@router.delete("/delete_user", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    login: str,
    use_case: DeleteUserUseCase = Depends(delete_user_use_case),
):
    try:
        return await use_case.execute(login=login)
    except UserNotFoundByLoginException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.get_detail()
        )

@router.get("/post/{id}", status_code=status.HTTP_200_OK, response_model=Post)
async def get_post_by_id(
    id: str,
    use_case: GetPostByIdUseCase = Depends(get_post_by_id_use_case),
) -> Post:
    try:
        return await use_case.execute(id=id)
    except PostNotFoundByIdException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.get_detail()
        )

@router.post("/create_post", status_code=status.HTTP_201_CREATED, response_model=Post)
async def create_post(
    post: Post,
    use_case: CreatePostUseCase = Depends(create_post_use_case),
) -> Post:
    try:
        return await use_case.execute(post=post)
    except PostIdIsNotUniqueException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exc.get_detail()
        )

@router.put("/change_post", status_code=status.HTTP_202_ACCEPTED, response_model=Post)
async def change_post(
    new_post: str,
    old_post_id: int,
    use_case: ChangePostUseCase = Depends(change_post_use_case),
) -> Post:
    try:
        return await use_case.execute(new_post=new_post, old_post_id=old_post_id)
    except PostIdIsNotUniqueException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exc.get_detail()
        )

@router.delete("/delete_post", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: int,
    use_case: DeletePostUseCase = Depends(delete_post_use_case)
):
    try:
        return await use_case.execute(id)
    except PostNotFoundByIdException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exc.get_detail()
        )