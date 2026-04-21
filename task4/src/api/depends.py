from domain.use_case.user.get_user_by_login import GetUserByLoginUseCase
from domain.use_case.user.create_user import CreateUserUseCase
from domain.use_case.user.delete_user import DeleteUserUseCase

from domain.use_case.post.get_post_by_id import GetPostByIdUseCase
from domain.use_case.post.create_post import CreatePostUseCase
from domain.use_case.post.delete_post import DeletePostUseCase
from domain.use_case.post.change_post import ChangePostUseCase

def get_user_by_login_use_case() -> GetUserByLoginUseCase:
    return GetUserByLoginUseCase()

def create_user_use_case() -> CreateUserUseCase:
    return CreateUserUseCase()

def delete_user_use_case() -> DeleteUserUseCase:
    return DeleteUserUseCase()

def get_post_by_id_use_case() -> GetPostByIdUseCase:
    return GetPostByIdUseCase()

def create_post_use_case() -> CreatePostUseCase:
    return CreatePostUseCase()

def change_post_use_case() -> ChangePostUseCase:
    return ChangePostUseCase()

def delete_post_use_case() -> DeletePostUseCase:
    return DeletePostUseCase()