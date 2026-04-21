from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.users import UserRepozitory
from shemas.users import User as UserShema
from core.exceptions.database_exceptions import UserNotFoundException
from core.exceptions.domain_exceptions import UserNotFoundByLoginException


class GetUserByLoginUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepozitory()

    async def execute(self, login: str) -> UserShema:
        try:
            with self._database.session() as session:
                user = self._repo.get(session=session, login=login)
        except UserNotFoundException:
            raise UserNotFoundByLoginException(login=login)
        return UserShema.model_validate(obj=user)