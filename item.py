#items

class Item(object):
    """Handle objects that can be obtained and used by the player."""
    def __init__(self, name):
        self.name = name

    def loot_for_item(self):
        pass
