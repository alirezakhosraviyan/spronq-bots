from .state_management import StateManager


class Bin(StateManager):
    def __init__(self, identifier):
        super().__init__(identifier)
