class Card_class:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction

class Creature(Card_class):
    def __init__(self, name, faction, attack, hp, cost, is_tapped):
        super().__init__(name, faction)
        self.attack     = attack
        self.hp         = hp
        self.cost       = cost
        self.is_tapped  = is_tapped

class Spell(Card_class):
    def __init__(self, name, faction, cost, effect):
        super().__init__(name, faction)
        self.cost = cost
        self.effect = effect

class Resource(Card_class):
    def __init__(self, name, faction, is_tapped):
        super().__init__(name, faction)
        self.is_tapped = is_tapped
