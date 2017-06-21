import random

class Player(object):
    """Keeps relevant data of player and handles behavior."""
    def __init__(self, name, gender, age, location, items, mount, agent_to_talk):
        self.name = name
        self.gender = gender
        self.age = age
        self.strength = age * float(random.uniform(1,2))
        self.hitpoints = age * float(random.uniform(1,2))
        self.items = items
        self.mount = mount
        self.agent_to_talk = agent_to_talk
        self.location = location

        '''
        # optional quick access        
        self.player_dict = {
            1 : self.name,
            2 : self.gender,
            3 : self.age,
            4 : self.strength,
            5 : self.hitpoints,
            6 : self.items,
            7 : self.mount,
            8 : self.location
        }'''
    
    def enter(self):
        pass

    def move(self, next_location):
        self.next_location = next_location

        self.location = self.next_location

        return self.location

    def talk_to(self, agent):
        self.agent = agent
        print ("\nMoechtest du ein Gespraech mit %s beginnen? (Ja / Nein)") % self.agent.name
        action = raw_input(">> ")
        if 'Ja' in action:
            self.agent.diag('Hallo')
        elif 'Nein' in action:
            self.agent.diag('Tschuess')
        else:
            print "Das habe ich nicht verstanden. Bitte antworte nur mit \"Ja\" oder \"Nein\"."

    def give_item_to(self, agent):
        self.agent = agent
        pass

    def take_item_from(self, agent):
        self.agent = agent
        pass

    def attack(self, agent):
        self.agent = agent
        pass

    def defend(self):
        pass

    def mount_(self, mount):
        self.mount = mount
        pass