from das_schwimmbad import *
from der_abwasserkanal import *

class Start(object):
    """Show intro and instructions to the game."""
    def __init__(self):
        print """
 _____                                      ___  _ _
|  ___|                            ___     / _ \| (_)
| |__ _ __ ___  _ __ ___   __ _   ( _ )   / /_\ \ |_  __ _
|  __| '_ ` _ \| '_ ` _ \ / _` |  / _ \/\ |  _  | | |/ _` |
| |__| | | | | | | | | | | (_| | | (_>  < | | | | | | (_| |
\____/_| |_| |_|_| |_| |_|\__,_|  \___/\/ \_| |_/_|_|\__,_|

        Herzlich willkommen zu Emma & Alia - Teil 1.
        Diese Geschichte heisst "An einem Sommertag".
        """

class Knockout(object):
    """docstring for Knockout."""
    def enter(self):
        print "Du bist k.o."
        action = raw_input("Moechtest du noch einmal spielen?\n>> ")
        if "Ja" in action:
            return "start"
        else:
            exit(1)


class Ende(object):
    """docstring for Ende."""
    def enter(self):
        print "Du hast gewonnen."
        exit(1)

class Map(object):
    """Spawn scenes and a list its locations."""

    scenes = {
        'start' : Start(),
        'knockout' : Knockout(),
        'ende' : Ende(),
    }

    scenemapper = {
        #Das Schwimmbad
        'start' : 'schwimmbad',
        'liegewiese' : 'schwimmbad',
        'gertudesbaum' : 'schwimmbad',
        'beckenrand' : 'schwimmbad',
        'sprungturm' : 'schwimmbad',
        'schwimmbecken' : 'schwimmbad',
        'imbiss' : 'schwimmbad',
        'kassenhaus' : 'schwimmbad',

        #Der Abwasserkanal
        'abwasserkanal' : 'abwasserkanal',
        'weggabelung' : 'abwasserkanal'
    }

    locations = {
        #Das Schwimmbad
        'liegewiese' : Liegewiese(),
        'gertudesbaum' : GertrudesBaum(),
        'beckenrand' : Beckenrand(),
        'sprungturm' : Sprungturm(),
        'schwimmbecken' : Schwimmbecken(),
        'imbiss' : Imbiss(),
        'kassenhaus' : Kassenhaus(),

        #Der Abwasserkanal
        'weggabelung' : Weggabelung(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def create_doors(self):
        "Tuer erstellt."

    def create_agents(self):
        pass
    
    def create_chests(self):
        pass

    def create_traps(self):
        pass

game_map = Map('start')
