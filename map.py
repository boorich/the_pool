class Map(object):
    """Spawn scenes and a list its locations."""

    scenes = {
    'start' : Start(),
    'knockout' : Knockout(),
    'ende' : Ende(),
    'schwimmbad' : Schwimmbad(),
    'abwasserkanal' : Abwasserkanal(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def create_doors(self):
        pass
