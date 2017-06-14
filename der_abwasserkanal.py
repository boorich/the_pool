#der Abwasserkanal

class Abwasserkanal(object):
    loc_index = 8
    def enter(self):
        if first_visit:
            print "Du bist im Abwasserkanal."
        else:
            print "Du warst schon eimal hier."
abwasserkanal = Abwasserkanal()

class Weggabelung(object):
    loc_index = 9
    def enter(self):
        if first_visit:
            print "Du bist an der Weggabelung im Abwasserkanal."
        else:
            print "Du warst schon eimal hier."
weggabelung = Weggabelung()
