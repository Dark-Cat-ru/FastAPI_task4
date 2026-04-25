from infrastructure.sqlite.database import database
from infrastructure.sqlite.repozitories.posts import PostRepozitory
from shemas.posts import Post as PostSchema
from core.exceptions.database_exceptions import PostAlreadyExistsException
from core.exceptions.domain_exceptions import PostIdIsNotUniqueException

class CreatePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepozitory()

    async def execute(self, post: PostSchema) -> PostSchema:
        try:
            with self._database.session() as session:
                new_post = self._repo.create(session=session, post=post)
        except PostAlreadyExistsException:
            raise PostIdIsNotUniqueException(id=post.id)
        return PostSchema.model_validate(obj=new_post)