from sys import exit
import random
import pickle

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
        return action

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

class Player(object):
    """Keeps relevant data of player and handles behavior."""
    def __init__(self, name, gender, age, items, mount):
        self.name = name
        self.gender = gender
        self.age = age
        self.strength = age * float(random.uniform(1,2))
        self.hitpoints = age * float(random.uniform(1,2))
        self.items = items
        self.mount = mount

        self.player_dict = {
        1 : self.name,
        2 : self.gender,
        3 : self.age,
        4 : self.strength,
        5 : self.hitpoints,
        6 : self.items,
        7 : self.mount
        }

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

class Engine(object):
    """Takes in the navigation, plays the game, handles savegames and players."""
    def __init__(self, navigation):
        self.navigation = navigation

    def playgame(self):
        """Show Textblock followed by Menu of available options."""
        print "-*" * 30
        action = str(menu.main_menu())
        print action
        if action is '0':
            self.create_player()
            raw_input('Moechtest du diesen Spieler jetzt abspeichernm dann druecke bitte die Enter Taste.')
            self.savegame()
            #implement: new_game()

        elif action is '1':
            pass
            #implement: load_game()
        elif action is '2':
            print 'Auf wiedersehen.'
            exit(1)
        else:
            print "Das habe ich nicht verstanden"

    def savegame(self):
        """write current state entire game session to a file."""
        pickle_out = open ("savegame.txt", 'w')
        player.player_dict = pickle.dump(player.player_dict, pickle_out)
        pickle_out.close()

    def loadgame(self):
        """Restore a game session based on a player name string."""
        pass

    def create_player(self):
        """define a new player name, gender and generate hitpoints randomly"""
        new_player = Player(raw_input('Dein Name: '), raw_input('Dein Geschlecht: '), float(raw_input('Dein Alter: ')), None, None)
        #help(new_player)
        print '\nDein Name lautet %s, du bist %s und %s jahre alt.' % (new_player.name, new_player.gender, int(new_player.age))
        print 'Daraus ergibt sich eine Angriffswert von %s und du erhaelts %s Lebenspunkte zu Beginn diese Spiels.\n' % (int(new_player.strength), int(new_player.hitpoints))
        global player
        player = new_player

    def delete_player(self, name):
        """truncate one players data from disk"""
        pass

the_navigation = Navigation(game_map)
#print help(the_navigation)
the_game = Engine(the_navigation)
#print help(the_game)
menu = Menu()
the_game.playgame()
