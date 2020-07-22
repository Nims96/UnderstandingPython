class Card_class:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction

    def list_iterator(self, zone):
        for x in zone:
            print(x.name)

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

    def cost_requirement(self, card, player):
        tmp = []
        
        print("The cost of the card you want to play is " + str(card.cost))
        print("These are you untapped Resources" + str(player.resource_untapped))
        
        while tmp != card.cost:
            for x in range(0, len(player.resource_untapped)):
                    print(str(x + 1) + ": " + player.resource_untapped[x])
            tmp_selection = int(input("Select a resource to add to the pool: "))

            player.resource_untapped[tmp_selection - 1]

            tmp = card.cost

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
