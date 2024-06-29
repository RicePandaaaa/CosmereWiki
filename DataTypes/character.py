
class Character():

    def __init__(self, name):
        # Identity
        self.name = name
        self.nicknames = []

        # Presence
        self.books = []
        self.titles = []

        # Relationships (name: relationship status)
        self.relationships = {}

        # Information
        self.info = ""
        self.notes = ""
        self.description = ""

    """
    Setter functions for string info
    """
    
    def set_name(self, name):
        self.name = name

    def set_info(self, info):
        self.info = info

    def set_notes(self, notes):
        self.notes = notes

    def set_description(self, description):
        self.description = description

    """
    Getter functions to get information
    """

    def get_name(self):
        return self.name
    
    def get_nicknames(self):
        return self.nicknames
    
    def get_books(self):
        return self.books
    
    def get_title(self):
        return self.titles
    
    def get_relationships(self):
        return self.relationships
    
    def get_info(self):
        return self.info
    
    def get_notes(self):
        return self.notes
    
    """
    Adder functions to add information
    """
    
    def add_nicknames(self, nickname):
        self.nicknames.append(nickname)
    
    def add_books(self, book):
        self.books.append(book)
    
    def add_title(self, title):
        self.titles.append(title)
    
    def add_relationships(self, relationship):
        self.relationships.append(relationship)

    def add_description(self, description):
        self.description.add(description)

    """
    Remover functions to remove information
    """
    
    def remove_nicknames(self, nickname):
        self.nicknames.remove(nickname)
    
    def remove_books(self, book):
        self.books.remove(book)
    
    def remove_title(self, title):
        self.titles.remove(title)
    
    def remove_relationships(self, relationship):
        self.relationships.remove(relationship)
