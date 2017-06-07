from sys import exit

import agent
import mount
import trap
import chest
import item
import game_map

class Menu(object):

    def main_menu(self):
        print """
        Neues Spiel   (0)
        Spiel laden   (1)
        Spiel beenden (2)
        """
        action = raw_input("Bitte waehle eine Option: ")
        return str(action)

    def context_menu(self):
        action = raw_input("Bitte waehle eine Option: ")
        return action

class Navigation(object):
    """Take in Map and handle all possible locations, track current location, find next possible location."""
    def __init__(self, gamemap):
        self.gamemap = gamemap

    def next_scene(self):
        """return a list of possible next scenes"""
        # current_scene =
        # next_scene =

    def available_locations(self):
        """return a list of available locations next scenes"""
        # available_locations =

class Engine(object):
    """Takes in the navigation, plays the game, handles savegames and players."""
    def __init__(self, navigation):
        self.navigation = navigation

    def playgame(self):
        """Show Textblock followed by Menu of available options."""
        menu.main_menu()
        print menu.action

    def loadgame(self):
        """Restore a game session based on a player name string."""
        pass

    def savegame(self):
        """write current state entire game session to a file."""
        pass

    def create_player(self):
        """define a new player name, gender and generate hitpoints randomly"""
        pass

    def delete_player(self):
        """truncate one players data from disk"""
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

the_navigation = Navigation(game_map)
#print help(the_navigation)
the_game = Engine(the_navigation)
#print help(the_game)
menu = Menu()
the_game.playgame()
