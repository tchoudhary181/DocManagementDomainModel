class Document: 
    def __init__ (self, doc_id:str, title:str, content:str, owner_id :str):
        self._doc_id = doc_id  # document's id (private)
        self._title = title    # document's title (private)
        self._content = content # document's content (private)
        self._owner_id  = owner_id  # document's owner id (private)

    def get_id(self) -> str:
        return self._doc_id

    def get_title(self) -> str:
        return self._title

    def get_owner(self) -> str:
        return self._owner_id

    def read(self) -> str:
        return self._content

    def update_content(self, new_content: str) -> None:
        self._content = new_content

    
    