#das schwimmbad

locations = {
'Liegewiese' : Liegewiese(),
'Gertrude\'s Baum' : GertrudesBaum(),
'Beckenrand' : Beckenrand(),
'Sprungturm' : Sprungturm(),
'Schwimmbecken' : Schwimmbecken(),
'Imbiss' : Imbiss(),
'Kassenhaus' : Kassenhaus(),
}

class Liegewiese(Location):
    loc_index = 0
    def enter(self):
        if first_visit:
            print "Du bist an Gertrudes Baum."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass

class GertrudesBaum(Location):
    loc_index = 1
    loc_name = 'Gertrude\'s Baum'
    def enter(self):
        if first_visit:
            print "Du bist an Gertrudes Baum."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass

class Beckenrand(Location):
    loc_index = 2
    loc_name = 'Beckenrand'
    def enter(self):
        if first_visit:
            print "Du bist Beckenrand."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass

class Sprungturm(Location):
    loc_index = 3
    loc_name = 'Sprungturm'
    def enter(self):
        if first_visit:
            print "Du bist am Sprungturm."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass

class Schwimmbecken(Location):
    loc_index = 4
    loc_name = 'Schwimmbecken'
    def enter(self):
        if first_visit:
            print "Du bist im Schwimmbecken."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass

class Imbiss(Location):
    loc_index = 5
    loc_name = 'Imbiss'
    def enter(self):
        if first_visit:
            print "Du bist am Imbiss."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass

class Kassenhaus(Location):
    loc_index = 6
    loc_name = 'Kassenhaus'
    def enter(self):
        if first_visit:
            print "Du bist am Kassenhaus."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass
