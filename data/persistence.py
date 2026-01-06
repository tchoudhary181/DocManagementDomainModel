import json
import os
from domain.user import User
from domain.document import Document

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")
DOCS_FILE = os.path.join(DATA_DIR, "documents.json")

os.makedirs(DATA_DIR, exist_ok=True)


def save_users(user_store):
    data = [
        {"id": u.get_id(), "name": u.get_name()}
        for u in user_store.list_users()
    ]
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)



def load_users(user_store):
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
        for item in data:
            user_store.add_user(User(item["id"], item["name"]))
    except FileNotFoundError:
        pass


def save_documents(document_store):
    data = []
    for doc in document_store._documents.values():
        data.append({
            "id": doc.get_id(),
            "title": doc.get_title(),
            "content": doc.read(),
            "owner": doc.get_owner()
        })
    with open(DOCS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)



def load_documents(document_store):
    try:
        with open(DOCS_FILE, "r") as f:
            data = json.load(f)
        for item in data:
            document_store.add_document(
                Document(
                    item["id"],
                    item["title"],
                    item["content"],
                    item["owner"]
                )
            )
    except FileNotFoundError:
        pass
