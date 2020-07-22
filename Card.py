class Card_class:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction

    def tap(self, card, untap_list, tap_list, position):
        if card.is_tapped == False:
            tap_list.append(untap_list[position])
            untap_list.pop(position)
            card.is_tapped = True

    def untap(self, card, untap_list, tap_list, position):
        if card.is_tapped == True:
            untap_list.append(tap_list[position])
            tap_list.pop(position)
            card.is_tapped = False

    #def cost_requirement(self, card):


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
