class Agent(object):
    """Keeps relevant data of NPC and handles behavior."""
    def __init__(self, name, hitpoints, strenght, location, item, detail):
        self.name = name
        self.hitpoints = hitpoints
        self.strenght = strenght
        self.location = location
        self.item = item
        self.detail = detail

    def move(self):
        '''move player around randomly within the level'''
        pass

    def talk(self):
        '''give answer based on input string'''
        pass

    def give_item(self):
        '''return an item object to the player'''
        pass

    def take_item(self):
        '''recieve an item object from player'''
        pass

    def attack(self):
        '''attack the player based on current strenght value'''
        pass

    def defend(self):
        '''defend agains an attack from the player'''
        pass
    
    def give_up(self):
        '''equivalent to dying, but less brutal (this is a kids game)'''
        pass
    
    def expose_details(self):
        print self.detail

alia = Agent('Alia', 50, 1,'liegewiese', None, 'Deine beste Freundin. Sie begleitet dich auf deinem Abenteuer.')
gertrude = Agent('Gertrude', 50, 1,'gertrudesbaum', None, 'Eine diebische Elster, die an einer funkelnden Haarspange interessiert ist. Sie kann dir helfen wenn du Ihr hilfst.')
dicker_junge = Agent('Marek', 50, 1,'sprungturm', None, 'Ein dicker Junge, der sich nicht traut vom Sprungturm zu springen. Ueberrede Ihn und er wird dir weiter helfen.')
keines_maedchen = Agent('Sophia', 50, 1,'beckenrand', None, 'Ein kleines Maedchen, dass seine Haarspange im Schwimmbecken verloren hat. Kannst du Ihr helfen?')
james = Agent('james', 50, 1, 'kassenhaus', None, 'Dein verfressener Bruder auf der Suche nach ein Cheeseburger. Fuetter ihn und er wird dir weiter helfen.')
gerald = Agent('Gerald', 50, 1, 'geraldsbaum', None, 'Ein Rabe, der den Weg zu Samira der Fee kennt. Beantwortest du seine 3 Fragen richtig, so hilft er dir.')
samira = Agent('samira', 50, 1, 'feenbrunnen', None, 'Eine maechtige Fee aus dem Land der Einhoerner. Sie kann Pferde in Einhoerner verzaubern. Gib ihr den Schatz aus dem Feenhort und sie verwandelt dein Pferd.')
lisa = Agent('lisa', 50, 1, 'reitplatz', None, 'Die Tochter vom Zahnarzt in Ludwigslsut und das verwoehnteste Maedchen von der ganzen Schule. Sie reitet nur mit Maedchen mit besonderen Pferden aus.')
bergtroll = Agent('Gronkh', 50, 1, 'zumbergpfad', None, 'Ein grimmiger Troll. Er ist sehr stark, gefaehrlich und laesst dich nicht vorbei. Trickse ihn aus.')
fledermaeuse = Agent('Die 3 Fledermaeuse', 50, 1, 'fledermausgrotte', None, '3 hungrige Fledermaeuse, vor denen du dich fuerchtest. Du kannst kaempfen oder versuchen sie zu vertreiben.')
kraehen = Agent('Die 3 Kraehen', 50, 1, 'kraehenbusch', None, '3 freche Kraehen, die dich beklauen. Du solltest ihnen eine Lektion erteilen.')

  