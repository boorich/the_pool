#der Abwasserkanal

locations = {
'Abwasserkanal' : Abwasserkanal(),
}

class Abwasserkanal(Location):
    global loc_index = 7
    def enter(self):
        if first_visit:
            print "Du bist im Abwasserkanal."
        elif:
            print "Du warst schon eimal hier."
        else:
            pass
