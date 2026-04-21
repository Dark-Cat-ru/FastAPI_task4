from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.posts import PostRepozitory
from shemas.posts import Post as PostShema
from core.exceptions.database_exceptions import PostNotFoundException
from core.exceptions.domain_exceptions import PostNotFoundByIdException


class GetPostByIdUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepozitory()

    async def execute(self, id: int) -> PostShema:
        try:
            with self._database.session() as session:
                post = self._repo.get_by_id(session=session, id=id)
        except PostNotFoundException:
            raise PostNotFoundByIdException(id=id)
        return PostShema.model_validate(obj=post)