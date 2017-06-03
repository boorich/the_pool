#der Abwasserkanal

class Abwasserkanal(object):
    loc_index = 7
    def enter(self):
        if first_visit:
            print "Du bist im Abwasserkanal."
        else:
            print "Du warst schon eimal hier."
abwasserkanal = Abwasserkanal()

locations = {
'Abwasserkanal' : abwasserkanal,
}
