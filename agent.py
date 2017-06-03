class Agent(object):
    """Keeps relevant data of NPC and handles behavior.
    * Alia
    * Gertrude, die Elster
    * dicker Junge
    * kleines Maedchen
    * James
    * Gerald, der Rabe
    * Samira, die Fee
    * Lisa
    * Bergtroll
    * Fledermaeuse
    * Kraehen
    """
    def __init__(self, name, hitpoints, strenght):
        self.name = name
        self.hitpoints = hitpoints
        self.strenght = strenght

    def move(self):
        pass

    def talk(self):
        pass

    def give_item(self):
        pass

    def take_item(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass
