from domain.user import User
from domain.document import Document
from domain.document_store import DocumentStore
from domain.user_store import UserStore
from data.persistence import (
    save_users, load_users,
    save_documents, load_documents
)


def main():
    user_store = UserStore()
    document_store = DocumentStore()

    load_users(user_store)
    load_documents(document_store)

    while True:
        print("\n--- Document Management System ---")
        print("1. Add user")
        print("2. Delete user")
        print("3. Create document")
        print("4. Read document")
        print("5. Update document")
        print("6. Delete document")
        print("7. List users")
        print("8. Exit")

        choice = input("Choose: ").strip()

        # Add user
        if choice == "1":
            uid = input("User ID: ")
            name = input("Name: ")
            try:
                user_store.add_user(User(uid, name))
                save_users(user_store)
                print("User added.")
            except ValueError as e:
                print(e)

        # Delete user
        elif choice == "2":
            uid = input("User ID to delete: ")
            try:
                user_store.remove_user(uid)
                save_users(user_store)
                print("User deleted.")
            except KeyError as e:
                print(e)

        # Create document
        elif choice == "3":
            doc_id = input("Document ID: ")
            title = input("Title: ")
            content = input("Content: ")
            owner = input("Owner ID: ")

            if not user_store.user_exists(owner):
                print("User does not exist.")
                continue

            document_store.add_document(
                Document(doc_id, title, content, owner)
            )
            save_documents(document_store)
            print("Document created.")

        # Read document
        elif choice == "4":
            doc_id = input("Document ID: ").strip()
            try:
                document = document_store.get_document(doc_id)
                print("\n--- Document Content ---")
                print(document.read())
                print("------------------------")
            except KeyError:
                print("Document not found.")
            

        # Update document
        elif choice == "5":
            doc_id = input("Document ID: ")
            content = input("New content: ")
            try:
                document_store.update_document(doc_id, content)
                save_documents(document_store)
                print("Document updated.")
            except KeyError:
                print("Document not found.")

        # Delete document
        elif choice == "6":
            doc_id = input("Document ID: ")
            try:
                document_store.remove_document(doc_id)
                save_documents(document_store)
                print("Document deleted.")
            except KeyError:
                print("Document not found.")

        elif choice == "7":
            for u in user_store.list_users():
                print(f"{u.get_id()} - {u.get_name()}")

        elif choice == "8":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
