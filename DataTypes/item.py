
class Item():
    def __init__(self, name):
        # Identity
        self.name = name
        self.nicknames = []

        # Origin
        self.creation = ""
        self.owner = None
        self.previous_owners = []

        # Description
        self.powers = []
        self.description = ""

    """
    Getter functions
    """

    def get_name(self):
        return self.name
    
    def get_nicknames(self):
        return self.nicknames
    
    def get_creators(self):
        return self.creators
    
    def get_owner(self):
        return self.owner
    
    def get_previous_owners(self):
        return self.previous_owners
    
    def get_powers(self):
        return self.powers
    
    def get_description(self):
        return self.description

    """
    Setter functions
    """

    def set_owner(self, owner):
        self.owner = owner

    def set_creation(self, creation):
        self.creation = creation

    def set_description(self, description):
        self.description = description

    """ 
    Adder functions
    """

    def add_nickname(self, nickname):
        self.nicknames.append(nickname)

    def add_previous_owner(self, previous_owner):
        self.previous_owners.append(previous_owner)

    def add_power(self, power):
        self.powers.append(power)

    """ 
    Remover functions
    """

    def remove_nickname(self, nickname):
        self.nicknames.remove(nickname)

    def remove_previous_owner(self, previous_owner):
        self.previous_owners.remove(previous_owner)

    def remove_power(self, power):
        self.powers.remove(power)
