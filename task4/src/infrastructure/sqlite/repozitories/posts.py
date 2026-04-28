from typing import Type

from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from infrastructure.sqlite.models.posts import Post as PostModel
from shemas.posts import Post as PostShema
from core.exceptions.database_exceptions import PostNotFoundException, PostAlreadyExistsException

class PostRepozitory:
    def __init__(self):
        self._model: Type[PostModel] = PostModel

    def get_by_id(self, session: Session, id: int):
        query = (
            select(self._model).where(self._model.id == id)
        )
        post = session.scalar(query)
        if not post:
            raise PostNotFoundException()
        return post

    def create(self, session: Session, post: PostShema) -> PostModel:
        query = (
            insert(self._model).values(post.model_dump()).returning(self._model)
        )
        try:
            return session.scalar(query)
        except IntegrityError:
            raise PostAlreadyExistsException()

    def delete(self, session: Session, id: int):
        post = session.query(PostModel).filter_by(id=id).first()
        if not post:
            raise PostNotFoundException()
        session.delete(post)
        session.commit()

    def change(self, session: Session, new_post: str, old_post_id: int) -> PostModel:
        old_post = session.scalar(select(self._model).where(self._model.id == old_post_id))
        if old_post is None:
            raise PostNotFoundException()
        old_post.text = new_post
        session.commit()
        session.refresh(old_post)
        return old_post