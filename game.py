import das_schwimmbad
import der_abwasserkanal

class Navigation(object):
    """Handle all possible locations, track current location, find next possible location."""
    def __init__(self, gamemap, scenemap):
        self.gamemap = gamemap
        self.scenemap = scenemap

    def next_scene(self):
        """return a list of possible next scenes"""
        pass

    def opening_scene(self):
        """return opening scene"""
        pass

class Engine(object):
    """Takes in the navigation, plays the game, handles savegames and players."""
    def __init__(self, arg):
        self.arg = arg

    def loadgame(self):
        pass

    def playgame(self):
        pass

    def savegame(self):
        pass

    def create_player(self):
        pass

    def delete_player(self):
        pass

class Location(object):
    """Spawn locations and a list its scenes."""

    locations = {
    'start' : Start(),
    'knockout' : Knockout(),
    'ende' : Ende(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def create_doors(self):
        pass

class Item(object):
    """Handle objects that can be obtained and used by the player."""
    def __init__(self, name):
        self.name = name

    def loot_for_item(self):
        pass

class Door(object):
    """Handle opening and closing of doors.
    * Offener Durchgang
    * Drehtür
    * Gitter
    * Normale Tür
    * Getarnter Durchgang
    * Schiebetür
    * Schwingtür
    """
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def open_door(self):
        pass

    def close_door(self):
        pass

    def lock_door(self):
        pass

class Chest(object):
    """Take in items and handle opening and closing of chests and loot.
    * Treasure Chest
    * Storage Chest
    """
    def __init__(self, name, content, key, type):
        self.name = name
        self.content = content

    def open_chest(self):
        pass

class Trap(object):
    """Handle state of trap, trigger it, calculate and return effect.
    * Holzbalken
    * Vereister See
    """
    def __init__(self, arg):
        self.arg = arg

    def snap(self):
        pass

class Agent(object):
    """Keeps relevant data of NPC and handles behavior.
    * Alia
    * Gertrude, die Elster
    * dicker Junge
    * kleines Mädchen
    * James
    * Gerald, der Rabe
    * Samira, die Fee
    * Lisa
    * Bergtroll
    * Fledermäuse
    * Krähen
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

class Player(object):
    """Keeps relevant data of player and handles behavior."""
    def __init__(self, name, gender, hitpoints, items, mount):
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

    def mount_horse(self):
        pass

class Mount(object):
    """Handle behavior and data of mounts
    * Ella
    * Fella
    * Gella
    * Pink-Po
    """
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def consume_food(self):
        pass

    def listern(self):
        pass
