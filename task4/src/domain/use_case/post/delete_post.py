from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.posts import PostRepozitory
from core.exceptions.database_exceptions import PostNotFoundException
from core.exceptions.domain_exceptions import PostNotFoundByIdException


class DeletePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepozitory()

    async def execute(self, id: int):
        try:
            with self._database.session() as session:
                self._repo.delete(session=session, id=id)
        except PostNotFoundException:
            raise PostNotFoundByIdException(id=id)