from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.users import UserRepozitory
from core.exceptions.database_exceptions import UserNotFoundException
from core.exceptions.domain_exceptions import UserNotFoundByLoginException


class DeleteUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepozitory()
    
    async def execute(self, login: str):
        try:
            with self._database.session() as session:
                self._repo.delete_user(session=session, login=login)
        except UserNotFoundException:
            raise UserNotFoundByLoginException(login=login)