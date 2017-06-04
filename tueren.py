#doors

class Door(object):
    """Handle opening and closing of doors.
    * Offener Durchgang
    * Drehtuer
    * Gitter
    * Normale Tuer
    * Getarnter Durchgang
    * Schiebetuer
    * Schwingtuer
    """
    def __init__(self, name, key):
        self.name = name
        self.key = key

    def open_door(self):
        pass

    def close_door(self):
        pass

    def lock_door(self):
        pass

Gitter = Door('Unterwassergitter', None)

doors = {
'gitter' : Gitter,
}
