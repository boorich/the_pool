class Agent(object):
    """Keeps relevant data of NPC and handles behavior."""
    def __init__(self, name, hitpoints, strenght, location, item, detail, temper, mobility):
        self.name = name
        self.hitpoints = hitpoints
        self.strenght = strenght
        self.location = location
        self.item = item
        self.detail = detail
        self.temper = temper
        self.mobility = mobility

    def move(self):
        '''move player around randomly within the level'''
        #self.location = random.location

    def diag (self, greeting):
        '''give answers based on input strings'''
        self.greeting = greeting

        if 'Hallo' in self.greeting:
            print '%s.' % self.agents_diag[0]
        elif 'Tschuess' in self.greeting:
            print self.greeting
        else:
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

alia = Agent('Alia', 50, 1,'liegewiese', None, 'Deine beste Freundin. Sie begleitet dich auf deinem Abenteuer.', 'friendly', 'static')
gertrude = Agent('Gertrude', 50, 1,'gertrudesbaum', None, 'Eine diebische Elster, die an einer funkelnden Haarspange interessiert ist. Sie kann dir helfen wenn du Ihr hilfst.', 'friendly', 'scripted')
dicker_junge = Agent('Marek', 50, 1,'sprungturm', None, 'Ein dicker Junge, der sich nicht traut vom Sprungturm zu springen. Ueberrede Ihn und er wird dir weiter helfen.', 'friendly', 'static')
keines_maedchen = Agent('Sophia', 50, 1,'beckenrand', None, 'Ein kleines Maedchen, dass seine Haarspange im Schwimmbecken verloren hat. Kannst du Ihr helfen?', 'friendly', 'static')
james = Agent('james', 50, 1, 'kassenhaus', None, 'Dein verfressener Bruder auf der Suche nach ein Cheeseburger. Fuetter ihn und er wird dir weiter helfen.', 'friendly', 'mobile')
gerald = Agent('Gerald', 50, 1, 'geraldsbaum', None, 'Ein Rabe, der den Weg zu Samira der Fee kennt. Beantwortest du seine 3 Fragen richtig, so hilft er dir.', 'friendly', 'static')
samira = Agent('samira', 50, 1, 'feenbrunnen', None, 'Eine maechtige Fee aus dem Land der Einhoerner. Sie kann Pferde in Einhoerner verzaubern. Gib ihr den Schatz aus dem Feenhort und sie verwandelt dein Pferd.', 'friendly', 'static')
lisa = Agent('lisa', 50, 1, 'reitplatz', None, 'Die Tochter vom Zahnarzt in Ludwigslsut und das verwoehnteste Maedchen von der ganzen Schule. Sie reitet nur mit Maedchen mit besonderen Pferden aus.', 'friendly', 'static')
bergtroll = Agent('Gronkh', 50, 1, 'zumbergpfad', None, 'Ein grimmiger Troll. Er ist sehr stark, gefaehrlich und laesst dich nicht vorbei. Trickse ihn aus.', 'aggro', 'static')
fledermaeuse = Agent('Die 3 Fledermaeuse', 50, 1, 'fledermausgrotte', None, '3 hungrige Fledermaeuse, vor denen du dich fuerchtest. Du kannst kaempfen oder versuchen sie zu vertreiben.', 'aggro', 'static')
kraehen = Agent('Die 3 Kraehen', 50, 1, 'kraehenbusch', None, '3 freche Kraehen, die dich beklauen. Du solltest ihnen eine Lektion erteilen.', 'aggro', 'static')
  

agents_dict = {

    'liegewiese' : alia,
    'gertrudesbaum' : gertrude,
    'sprungturm' : dicker_junge,
    'kassenhaus' : james,
    'beckenrand' : keines_maedchen,
    'geraldsbaum' : gerald,
    'feenbrunnen' : samira,
    'reitplatz' : lisa,
    'zumbergpfad' : bergtroll,
    'fledermausgrotte' : fledermaeuse,
    'kraehenbusch' : kraehen
}

agents_diag = {

    alia : ['Ich helfe dir, wann immer du meinen Namen sagst.', 'D2', 'D3'],
    gertrude : ['Ich will eine funkelnde Haarspange.', 'D2', 'D3'],
    dicker_junge : ['Ich traue mich nicht vom Sprungturm zu springen', 'D2', 'D3'],
    james : ['Ich moechte einen Cheeseburger.', 'D2', 'D3'],
    keines_maedchen : ['Ich weiss das meine Haarspange in das Schwimmbecken gefallen ist.', 'D2', 'D3'],
    gerald : ['Loese ein Raetsel, damit ich dich zu Samira lasse.', 'D2', 'D3'],
    samira : ['Ich moechte den Schmuck aus der Truhe.', 'D2', 'D3'],
    lisa : ['Ich reite nur mit Freundinnen aus die besondere Pferde haben.', 'D2', 'D3'],
    bergtroll : ['Ich lasse dich nicht durch und ich habe Hunger auf Kaese.', 'D2', 'D3'],
    fledermaeuse : ['Wir stehlen deine Sachen und wir lassen dich nicht durch.', 'D2', 'D3'],
    kraehen : ['Wir wollen mit dir kaempfen und lassen dich nicht durch.', 'D2', 'D3'],
}