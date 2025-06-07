from .art import logo
class AnsiiArt:
    def __init__(self):
        self._logo = logo

    @property
    def logo(self):
        return self._logo
