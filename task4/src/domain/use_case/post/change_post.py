from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.posts import PostRepozitory
from shemas.posts import Post as PostSchema
from core.exceptions.database_exceptions import PostAlreadyExistsException, PostNotFoundException
from core.exceptions.domain_exceptions import PostIdIsNotUniqueException, PostNotFoundByIdException

class ChangePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepozitory()

    async def execute(self, new_post: str, old_post_id: int) -> PostSchema:
        try:
            with self._database.session() as session:
                post = self._repo.change(session=session, new_post=new_post, old_post_id=old_post_id)
        except PostAlreadyExistsException:
            raise PostIdIsNotUniqueException(id=old_post_id)
        return PostSchema.model_validate(obj=post)