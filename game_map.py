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
    def __init__(self):
        pass

class Ende(object):
    """docstring for Ende."""
    def __init__(self):
        pass

class Map(object):
    """Spawn scenes and a list its locations."""

    scenes = {
    'start' : Start(),
    'knockout' : Knockout(),
    'ende' : Ende(),
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
        pass

game_map = Map('start')
