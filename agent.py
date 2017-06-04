class Agent(object):
    """Keeps relevant data of NPC and handles behavior."""
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

alia = Agent('Alia', 50, 1)
gertrude = Agent('Gertrude', 50, 1)
dicker_junge = Agent('Marek', 50, 1)
keines_maedchen = Agent('Sophia', 50, 1)
james = Agent('james', 50, 1)
gerald = Agent('Gerald', 50, 1)
samira = Agent('samira', 50, 1)
lisa = Agent('lisa', 50, 1)
bergtroll = Agent('Gronkh', 50, 1)
fledermaeuse = Agent('Die 3 Fledermaeuse', 50, 1)
kraehen = Agent('Die 3 Kraehen', 50, 1)
