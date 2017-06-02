import stuff

class Navigation(object):
    """Handle all possible locations, track current location, find next possible location."""
    def __init__(self, gamemap, scenemap):
        self.gamemap = gamemap
        self.scenemap = scenemap

    def next_scene():
        """return a list of possible next scenes"""
        pass

    def opening_scene():
        """return opening scene"""
        pass

class Engine(object):
    """Takes in the navigation, plays the game, handles savegames and players."""
    def __init__(self, arg):
        self.arg = arg

    def loadgame():
        pass

    def playgame():
        pass

    def savegame():
        pass

    def create_player():
        pass

    def delete_player():
        pass

class Items(object):
    """Handle objects that can be obtained and used by the player."""
    def __init__(self, arg):
        self.arg = arg


    Items:
    * Haarspange
    * Cheeseburger
    * Brotkrumen
    * Käse
    * Hundepfeife
    * Reitgerte
    * Pferdeshampoo
    * Waschbürste
    * Heu
    * Apfel
    * Karotte
    * Sattel

Scene
- enter
* Start Game
* Knock Out
* Das Schwimmbad
 * Handtücher
 * Getrudes Baum
 * Sprungturm
 * Beckenrand
 * Burgerladen
 * Pool
* der Abwasserkanal
 * Wegkreuzung
* die Steilküste
 * Kante
 * Holzbalken
* die Zisterne
* der Schatzraum
* der geheime Krater
 * Höhlenausgang
 * am vereisten See
 * am Bergtroll
* der dunkle Pfad
 * bei den Fledermäusen
 * bei den Krähen
* der Park
 * Klettergrüst
 * Wippe
 * Geralds Baum
* der Feenhort
 * am Brunnen
 * am Schatz
* der Reitstall
 * Putzplatz
 * Sattelkammer
 * Futterecke
* der Reitplatz

Door
- open_door
- close_door
* Offener Durchgang
* Drehtür
* Gitter
* Normale Tür
* Getarnter Durchgang
* Schiebetür
* Schwingtür

Chests
- open_chest
- close_chest
- contain_item
* Treasure Chest
* Storage Chest

NPCs
- move
- talk
- give_item
- take_item
* Alia
* Gertrude, die Elster
* dicker Junge
* kleines Mädchen
* James
* Gerald, der Rabe
* Samira, die Fee
* Lisa
* Bergtroll
* Fledermäuse
* Krähen

Player
- talk
- move
- give_item
- take_item
* Name
* Gender
* Position
* Items
* Mount

Trap
- snap
- trigger_effect
* Holzbalken
* Vereister See

Mount
- listen
- move
- consume_food
* Ella
* Fella
* Gella
* Pink-Po
