from doors import *
from agent import *
from mount import *

doors = {

'to_kanal' : uwgitter

}

class Liegewiese(object):
    loc_index = 0
    first_visit = True

    def enter(self):
        if self.first_visit:
            print "Du befindest die auf der Liegewiese des Schwimmbads. Neben dir ist deine Freundin %s" % alia.name
            print "Die Sonne scheint hell und es ist sehr warm. Euer Liebeplatz befindet sich in der Naehe des Zauns."
            print "Auf der andere Seite des Zauns siehst du einen Reitplatz. Ein Maedchen kommt gerade auf den Platz."
            print "Sie hat ein wunderschoenes Pferd an den Zuegeln, welches gutmuetig hinter Ihr her trottet."
            print "Als du genauer hin siehst faellt dir auf, dass es sich um deine Freundin %s mit Ihrem Pferd %s handelt" % (lisa.name, pink_po.name)
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
liegewiese = Liegewiese()

class GertrudesBaum(object):
    loc_index = 1
    loc_name = 'Gertrude\'s Baum'

    def enter(self):
        if first_visit:
            print "Du bist an Gertrudes Baum."
        else:
            print "Du warst schon eimal hier."
gertudesbaum = GertrudesBaum()

class Beckenrand(object):
    loc_index = 2
    loc_name = 'Beckenrand'
    def enter(self):
        if first_visit:
            print "Du bist Beckenrand."
        else:
            print "Du warst schon eimal hier."
beckenrand = Beckenrand()

class Sprungturm(object):
    loc_index = 3
    loc_name = 'Sprungturm'
    def enter(self):
        if first_visit:
            print "Du bist am Sprungturm."
        else:
            print "Du warst schon eimal hier."
sprungturm = Sprungturm()

class Schwimmbecken(object):
    loc_index = 4
    loc_name = 'Schwimmbecken'
    def enter(self):
        if first_visit:
            print "Du bist im Schwimmbecken."
        else:
            print "Du warst schon eimal hier."
schwimmbecken = Schwimmbecken()

class Imbiss(object):
    loc_index = 5
    def enter(self):
        if first_visit:
            print "Du bist am Imbiss."
        else:
            print "Du warst schon eimal hier."
imbiss = Imbiss()

class Kassenhaus(object):
    loc_index = 6
    def enter(self):
        if first_visit:
            print "Du bist am Kassenhaus."
        else:
            print "Du warst schon eimal hier."
kassenhaus = Kassenhaus()
