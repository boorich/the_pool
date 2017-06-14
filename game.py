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

player = None


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

    def locations_menu(self, location, game_map):
        self.location = location
        self.game_map = game_map
        print "Du bst an diesem Ort: %s " % self.location
        print "Von hier kannst du folgende Orte besuchen: "
        #print "Die Map: %s" % self.game_map
    

        poi_list = []
        for k, v in self.game_map.scenemapper.iteritems():
            if v == self.location:
                poi_list.append(k)

        def poi_format(poi_list):
            for i in poi_list:
                print i + '\n'
        
        poi_formatted = poi_format(poi_list)
        return poi_formatted


class Navigation(object):
    """Take in Map and the player handle all possible locations, track current location, find next possible location."""
    def __init__(self, gamemap):
        #self.player = player
        self.gamemap = gamemap

    def next_scene(self, last_scene):
        """return a list of possible next scenes"""
        available_locations = {}
        for k, v in the_navigation.gamemap.scenemapper.iteritems():
            available_locations.setdefault(v, []).append(k)
              
        for k, v in available_locations.iteritems():
            if the_game.player[8] in v:
                return k
        
        '''
        #noble way to check if string is in dictionary       
        if 'start' in [x for v in available_locations.values() for x in v]:
            #do something
        '''

class Engine(object):
    """Takes in the navigation, plays the game, handles savegames and players."""
    def __init__(self, navigation, the_player, the_menu):
        self.navigation = navigation
        self.player = the_player
        self.menu = the_menu

    def playgame(self):
        """Show Textblock followed by Menu of available options."""
        styles.flower()
        action = str(the_menu.main_menu())
        if action is '0':
            self.player = self.create_player()
            raw_input('Moechtest du diesen Spieler jetzt abspeichern, dann druecke bitte die Enter Taste.')
            self.savegame()
            self.player = self.loadinstant(self.player)
        elif action is '1':
            self.player = self.loadgame()
            print "\nHier beginnt deine Reise, %s. ich oeffne jetzt das Tor zu deinem Abenteuer." % self.player[1]
        elif action is '2':
            print 'Auf wiedersehen.'
            exit(1)
        else:
            print "Das habe ich nicht verstanden"

        #print "Du bist im %s. Hier gibt es folgende Orte, an denen du dich umsehen koenntest." % the_navigation.next_scene(self.player[8])
        print the_menu.locations_menu(the_navigation.next_scene(self.player[8]), game_map)

    def create_player(self):
        """define a new player name, gender and generate hitpoints randomly"""
        self.player = Player(raw_input('Dein Name: '), raw_input('Dein Geschlecht: '), float(raw_input('Dein Alter: ')), raw_input('Dein Start: '), None, None)
        #help(new_player)
        print '\nDein Name lautet %s, du bist %s und %s jahre alt.' % (self.player.name, self.player.gender, int(self.player.age))
        print 'Daraus ergibt sich eine Angriffswert von %s und du erhaelts %s Lebenspunkte zu Beginn dieses Spiels.\n' % (int(self.player.strength), int(self.player.hitpoints))
        return self.player

    def savegame(self):
        """write current state entire game session to a file."""
        pickle_out = open ('savegame_' + str(self.player.name) + '.txt', 'w+')
        self.player.player_dict = pickle.dump(self.player.player_dict, pickle_out)
        pickle_out.close()
        print "\nSpieler >> %s << gespeichert.\n" % self.player.name

    def loadgame(self):
        """Restore a game session based on a raw input of player name string."""
        savegames = glob("savegame*") #creates a list of available savegames on disk
        print "Du moechtest ein Spiel laden? In Ordnung, bitte waehle deinen Spieler:\n"
        for entries in savegames:
            #to do: format the strings to only display the name of the player
            print "        %s\n" % entries.rstrip('.txt').lstrip('savegame_')
        action = raw_input('>> ')
        pickle_in = open ('savegame_' + action + '.txt', 'r+')
        self.player = pickle.load(pickle_in)
        styles.flower()
        print "In Ordnung, %s. Legen wir los." % self.player[1]
        print '''
        Hier siehst du Details ueber deinen Helden:
        
        Name:           %s
        Geschlecht:     %s
        Alter:          %s Jahre
        Angriff:        %s
        Lebenspunkte:   %s
        Reittier:       %s

        Aktueller Ort:  %s
        ''' % (self.player[1], self.player[2], int(self.player[3]), int(self.player[4]), int(self.player[5]), self.player[7], self.player[8])
        
        return self.player

    def loadinstant(self, player):
        """Restore a game session based on a passed player name string."""
        player = self.player.name
        pickle_in = open ('savegame_' + player + '.txt', 'r+')
        restored_player = pickle.load(pickle_in)
        styles.flower()
        print "In Ordnung, %s. Legen wir los." % restored_player[1]
        print '''
        Hier siehst du Details ueber deinen Helden:
        
        Name:           %s
        Geschlecht:     %s
        Alter:          %s Jahre
        Angriff:        %s
        Lebenspunkte:   %s
        Reittier:       %s

        Aktueller Ort:  %s
        ''' % (restored_player[1], restored_player[2], int(restored_player[3]), int(restored_player[4]), int(restored_player[5]), restored_player[7],restored_player[8])

        return restored_player

    def delete_player(self, name):
        """truncate one players data from disk"""
        pass


styles = Styles(None)
the_menu = Menu(styles)
the_menu.styles.flower

the_player = Player(1, 2, 3, 4, 5, 6)
the_navigation = Navigation(game_map)
the_game = Engine(the_navigation, the_player, the_menu)

the_game.playgame()

'''
knockout = Knockout()
knockout.enter()

ende = Ende()
ende.enter()
'''
