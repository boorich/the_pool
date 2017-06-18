from doors import *
from agent import *
from mount import *


doors = {

'to_kanal' : uwgitter

}

class Liegewiese(object):
    loc_index = 0
    first_visit = True

    def __init__(self, agent, chest, doors, mount, trap):
        self.agent = agent
        self.chest = chest
        self.doors = doors
        self.mount = mount
        self.trap = trap

    def enter(self):
        if self.first_visit:
            print "Du befindest die auf der Liegewiese des Schwimmbads. Neben dir ist deine Freundin %s" % alia.name
            print "Die Sonne scheint hell und es ist sehr warm. Euer Liebeplatz befindet sich in der Naehe des Zauns."
            print "Auf der andere Seite des Zauns siehst du einen Reitplatz. Ein Maedchen kommt gerade auf den Platz."
            print "Sie hat ein wunderschoenes Pferd an den Zuegeln, welches gutmuetig hinter Ihr her trottet."
            print "Als du genauer hin siehst faellt dir auf, dass es sich um %s mit Ihrem Pferd %s handelt" % (lisa.name, pink_po.name)
            print "Ploetzlich kommt die ein Gedanke. Du springst auf und %s schaut dich fragend an:" % alia.name
            print "\"Lass uns reiten gehen\" rufst du %s vergnuegt entgegen und rennst los." % alia.name



        else:
            print "Du warst schon eimal hier."
            
liegewiese = Liegewiese(alia, None, None, None, None)

class GertrudesBaum(object):
    loc_index = 1
    first_visit = True
    loc_name = 'Gertrude\'s Baum'

    def enter(self):
        if self.first_visit:
            print "Du bist an Gertrudes Baum."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
gertrudesbaum = GertrudesBaum()

class Beckenrand(object):
    loc_index = 2
    first_visit = True
    loc_name = 'Beckenrand'
    def enter(self):
        if self.first_visit:
            print "Du bist Beckenrand."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
beckenrand = Beckenrand()

class Sprungturm(object):
    loc_index = 3
    first_visit = True
    loc_name = 'Sprungturm'
    def enter(self):
        if self.first_visit:
            print "Du bist am Sprungturm."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
sprungturm = Sprungturm()

class Schwimmbecken(object):
    loc_index = 4
    first_visit = True
    loc_name = 'Schwimmbecken'
    def enter(self):
        if self.first_visit:
            print "Du bist im Schwimmbecken."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
schwimmbecken = Schwimmbecken()

class Imbiss(object):
    loc_index = 5
    first_visit = True
    def enter(self):
        if self.first_visit:
            print "Du bist am Imbiss."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
imbiss = Imbiss()

class Kassenhaus(object):
    loc_index = 6
    first_visit = True
    def enter(self):
        if self.first_visit:
            print "Du bist am Kassenhaus."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
kassenhaus = Kassenhaus()
