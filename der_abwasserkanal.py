#der Abwasserkanal

class Abwasserkanal(object):
    loc_index = 8
    first_visit = True
    def enter(self):
        if self.first_visit:
            print "Du bist im Abwasserkanal."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
abwasserkanal = Abwasserkanal()

class Weggabelung(object):
    loc_index = 9
    first_visit = True
    def enter(self):
        if self.first_visit:
            print "Du bist an der Weggabelung im Abwasserkanal."
            self.first_visit = False
        else:
            print "Du warst schon eimal hier."
weggabelung = Weggabelung()
