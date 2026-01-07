from typing import Dict, List
from uuid import UUID

from domain.user import User
from domain.document import Document



class DocumentStore:
    """
    Acts as an in-memory repository.
    Later phases will replace this with a DB layer.
    """

    def __init__(self):
        self._users: Dict[UUID, User] = {}
        self._documents: Dict[UUID, Document] = {}

    # -------- User Operations --------
    def add_user(self, user: User) -> None:
        self._users[user.id] = user

    def get_user(self, user_id: UUID) -> User:
        user = self._users.get(user_id)
        if not user:
            raise UserNotFoundError("User does not exist")
        return user

    # -------- Document Operations --------
    def add_document(self, document: Document) -> None:
        if document.owner_id not in self._users:
            raise UserNotFoundError("Cannot create document for unknown user")
        self._documents[document.id] = document

    def get_document(self, document_id: UUID, requester_id: UUID) -> Document:
        document = self._documents.get(document_id)
        if not document:
            raise DocumentNotFoundError("Document not found")

        if document.owner_id != requester_id:
            raise PermissionDeniedError("Access denied to this document")

        return document

    def get_user_documents(self, user_id: UUID) -> List[Document]:
        if user_id not in self._users:
            raise UserNotFoundError("User does not exist")

        return [
            doc for doc in self._documents.values()
            if doc.owner_id == user_id
        ]
