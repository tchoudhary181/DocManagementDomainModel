from uuid import UUID, uuid4
from datetime import datetime


class Document:
    def __init__(self, owner_id: UUID, title: str, content: str):
        self._id: UUID = uuid4()
        self._owner_id = owner_id
        self._title = title
        self._content = content
        self._created_at = datetime.utcnow()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def owner_id(self) -> UUID:
        return self._owner_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def __repr__(self) -> str:
        return f"Document(id={self._id}, title={self._title})"
