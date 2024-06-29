
class Material():

    def __init__(self, name):
        # Identity
        self.name = name
        self.nicknames = []

        # Properties
        self.source = ""
        self.appearance = ""
        self.usages = ""
        self.description = ""

        # Book source
        self.book_source = ""

    """
    Getter functions
    """

    def get_name(self):
        return self.name
    
    def get_nicknames(self):
        return self.nicknames
    
    def get_source(self):
        return self.source
    
    def get_appearance(self):
        return self.appearance
    
    def get_usages(self):
        return self.usages
    
    def get_description(self):
        return self.description
    
    def get_book_source(self):
        return self.book_source
    
    """
    Setter functions
    """

    def set_name(self, name):
        self.name = name

    def set_source(self, source):
        self.source = source

    def set_appearance(self, appearance):
        self.appearance = appearance

    def set_usages(self, usages):
        self.usages = usages

    def set_description(self, description):
        self.description = description

    def set_book_source(self, book_source):
        self.book_source = book_source

    """
    Adder functions
    """

    def add_nickname(self, nickname):
        self.nicknames.append(nickname)

    """
    Remover functions
    """

    def remove_nickname(self, nickname):
        self.nicknames.remove(nickname)

    