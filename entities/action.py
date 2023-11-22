class Action:
    def __init__(self, name: str, effect: callable, description: str = ""):
        self._name = name
        self._effect = effect
        self._description = description

    @property
    def name(self):
        return self._name
    
    @property
    def effect(self):
        return self._effect

    @property
    def description(self):
        return self._description
    
    @effect.setter
    def effect(self, effect: callable):
        self._effect = effect

class Irrigate(Action):
    def __init__(self, name: str, effect: callable, description: str = ""):
        super().__init__(name, effect, description)
    