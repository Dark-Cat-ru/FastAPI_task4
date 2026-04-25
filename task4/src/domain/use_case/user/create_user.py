from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.users import UserRepozitory
from shemas.users import CreateUser, User as UserSchema
from core.exceptions.database_exceptions import UserAlreadyExistsException
from core.exceptions.domain_exceptions import UserLoginIsNotUniqueException


class CreateUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepozitory()

    async def execute(self, user: CreateUser) -> UserSchema:
        try:
            with self._database.session() as session:
                new_user = self._repo.create(session=session, user=user)
        except UserAlreadyExistsException:
            raise UserLoginIsNotUniqueException(login=user.login)
        return UserSchema.model_validate(obj=new_user)