#das schwimmbad

class Liegewiese(object):
    loc_index = 0
    def enter(self):
        if first_visit:
            print "Du bist an Gertrudes Baum."
        else:
            print "Du warst schon eimal hier."

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

locations = {
'Liegewiese' : Liegewiese(),
'Gertrude\'s Baum' : GertrudesBaum(),
'Beckenrand' : Beckenrand(),
'Sprungturm' : Sprungturm(),
'Schwimmbecken' : Schwimmbecken(),
'Imbiss' : Imbiss(),
'Kassenhaus' : Kassenhaus(),
}
