import os
from sys import exit
from glob import glob 
import pickle

from player import *
from styles import *
from agent import *
from mount import *
from trap import *
from chest import *
from item import *
from game_map import *

class Menu(object):

    def __init__(self, styles):
        self.styles = styles

    def menu_handler(self):
        """Take in return strings and display context menus accordingly."""
        action = return_string
        return action

    def main_menu(self):
        print """
        Neues Spiel   (0)
        Spiel laden   (1)
        Spiel beenden (2)
        """
        action = raw_input("Bitte waehle eine Option: ")
        print "\n"
        styles.flower()
        return action

    def help_menu(self):
        print"""
        Spiel verlassen     (Strg+C)
        Hauptmenue           (Home)
        """

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
        styles.flower()
        action = str(menu.main_menu())
        if action is '0':
            player = self.create_player()
            print player
            raw_input('Moechtest du diesen Spieler jetzt abspeichern, dann druecke bitte die Enter Taste.')
            self.savegame()
        elif action is '1':
            player = self.loadgame()
            print "\nHier beginnt deine Reise, %s. ich oeffne das entsprechende File fuer dich." % player[1]
        elif action is '2':
            print 'Auf wiedersehen.'
            exit(1)
        else:
            print "Das habe ich nicht verstanden"
        print "Das Spiel beginnt hier: %s" % player.location
        the_navigation.next_scene()

    def create_player(self):
        """define a new player name, gender and generate hitpoints randomly"""
        new_player = Player(raw_input('Dein Name: '), raw_input('Dein Geschlecht: '), float(raw_input('Dein Alter: ')), raw_input('Dein Startpunkt: '), None, None)
        #help(new_player)
        print '\nDein Name lautet %s, du bist %s und %s jahre alt.' % (new_player.name, new_player.gender, int(new_player.age))
        print 'Daraus ergibt sich eine Angriffswert von %s und du erhaelts %s Lebenspunkte zu Beginn diese Spiels.\n' % (int(new_player.strength), int(new_player.hitpoints))
        global player
        player = new_player
        return player

    def savegame(self):
        """write current state entire game session to a file."""
        pickle_out = open ('savegame_' + str(player.name) + '.txt', 'w+')
        player.player_dict = pickle.dump(player.player_dict, pickle_out)
        pickle_out.close()
        print "\nSpieler >> %s << gespeichert.\n" % player.name#
        styles.flower()

    def loadgame(self):
        """Restore a game session based on a player name string."""
        savegames = glob("savegame*") #creates a list of available savegames on disk
        print "Du moechtest ein Spiel laden? In Ordnung, bitte waehle deinen Spieler:\n"
        for entries in savegames:
            #to do: format the strings to only display the name of the player
            print "        %s\n" % entries.rstrip('.txt').lstrip('savegame_')
        action = raw_input('>> ')
        pickle_in = open ('savegame_' + action + '.txt', 'r+')
        restored_player = pickle.load(pickle_in)
        styles.flower()
        print "In Ordnung, %s. Legen wir los." % restored_player[1]
        print restored_player
        return restored_player

    def delete_player(self, name):
        """truncate one players data from disk"""
        pass

the_navigation = Navigation(game_map)

the_game = Engine(the_navigation)


styles = Styles(None)

menu = Menu(styles)
menu.styles.flower


the_game.playgame()

knockout = Knockout()
knockout.enter()

ende = Ende()
ende.enter()

