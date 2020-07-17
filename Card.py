class Card_class:
    def __init__(self, name, faction, description):
        self.name = name
        self.faction = faction
        self.description = description

class Creature(Card_class):
    def __init__(self, name, faction, description, attack, hp, cost, is_tapped):
        super().__init__(name, faction, description)
        self.attack     = attack
        self.hp         = hp
        self.cost       = cost
        self.is_tapped  = is_tapped

class Spell(Card_class):
    def __init__(self, name, faction, description, cost, effect):
        super().__init__(name, faction, description)
        self.cost = cost
        self.effect = effect

class Resource(Card_class):
    def __init__(self, name, faction, description, is_tapped):
        super().__init__(name, faction, description)
        self.is_tapped = is_tapped
