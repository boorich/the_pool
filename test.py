'''#strings
print "Provide a number x",
x = raw_input()
print "Provide a second number y",
y = raw_input()
z = x + y
print "%s + %s = %s, because raw_input() reads them in as strings" % (x, y, z)

#integers
print "Provide a number x",
x = int(raw_input())
print "Provide a second number y",
y = int(raw_input())
z = x + y
print "%s + %s = %s, because raw_input() reads tehm in as strings" % (x, y, z)'''

class Song(object):
    def __int__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()