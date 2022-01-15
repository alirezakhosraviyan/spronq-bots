import abc
from .micro_chip import MicroChip


class StateManager(metaclass=abc.ABCMeta):
    """

    """
    identifier = None
    _state: [MicroChip] = None

    def __init__(self, identifier):
        self._state: [MicroChip] = []
        self.identifier = identifier

    def __len__(self):
        return len(self._state)

    @property
    def state(self) -> [MicroChip]:
        return self._state

    @state.setter
    def state(self, new_state: MicroChip) -> None:
        if new_state is None:
            return

        self._state.append(new_state)

    def update_state(self, new_state: MicroChip) -> [MicroChip]:
        if new_state is None or new_state is list:
            return

        self._state.append(new_state)