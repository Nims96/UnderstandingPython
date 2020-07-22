class player_class:
    def __init__(self,player_turn,health):
        self.health = health
        self.player_turn = player_turn
        self.hand = []
        self.deck = []
        self.creature_tapped = []
        self.creature_untapped = []
        self.resource_tapped = []
        self.resource_untapped = []
        self.discard = []
        self.banished = []


