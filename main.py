from domain.user import User
from domain.document import Document
from domain.document_store import DocumentStore

alice = User("u1", "Alice")
bob = User("u2", "Bob")
charlie = User("u3", "Charlie")

# Create documents
doc1 = Document("d1", "Notes", "Python OOP basics", alice.get_id())
doc2 = Document("d2", "Todo", "Finish assignment", bob.get_id())
doc3 = Document("d3", "Maths Notes", "Start assignment", charlie.get_id())

store = DocumentStore()
store.add_document(doc1)
store.add_document(doc2)
store.add_document(doc3)

# Read a document
print(store.get_document("d1").read())
print(store.get_document("d2").read())
print(store.get_document("d3").read())

# List documents by user
alice_docs = store.get_documents_by_user("u1")
for doc in alice_docs:
    print(doc.get_title())

bob_docs = store.get_documents_by_user("u2")
for doc in bob_docs:
    print(doc.get_title())
        
charlie_docs = store.get_documents_by_user("u3")
for doc in charlie_docs:
    print(doc.get_title())

# update document
store.update_document("d2", "Bob's changes")
print("\nUpdated d2:")
print(store.get_document("d2").read())

#remove document
store.remove_document("d1")
print("\nd1 removed successfully")