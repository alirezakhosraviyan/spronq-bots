from .micro_chip import MicroChip
from .state_management import StateManager


class Pipe:
    """

    """
    output_dst: 'Bot' = None

    def __init__(self, output_dst):
        self.output_dst = output_dst

    def write_to_pip(self, micro_chip: MicroChip):
        self.output_dst.update_state(micro_chip)


class Bot(StateManager):

    identifier = None
    pipes = [Pipe]
    rules = [str]

    def __init__(self, identifier, pipes: [Pipe]):
        super(Bot, self).__init__(identifier)
        self.pipes: [Pipe] = pipes
        self.rules: [str] = []

    def update_state(self, new_state: MicroChip) -> [MicroChip]:
        if new_state is None or new_state is list:
            return

        self._state.append(new_state)

        # End-Condition of recursive function
        if len(self.state) == 2:
            self.process_state()

    def find_rule(self, rule_name) -> [str]:
        return next((rule for rule in self.rules if str(rule).startswith(rule_name)), '').split('_')

    def find_pipe(self, pipe_type: str, pipe_identifier) -> Pipe:
        tmp = next((pipe for pipe in self.pipes if type(pipe.output_dst).__name__.lower() == pipe_type.lower()
                     and pipe.output_dst.identifier == pipe_identifier), None)

        if tmp is None:
            print('eeeeee', pipe_type)
        return tmp

    @classmethod
    def __compare_numbers(cls, inp_list) -> (int, int):
        sorted_list = sorted(inp_list)
        return sorted_list[1], sorted_list[0]

    def flush_state(self) -> None:
        self.state = []

    def process_state(self) -> None:

        # End-Condition of recursive function
        # Force-Stop mistake function calls
        if len(self.state) != 2:
            print((self.identifier, 'stop'), end='')
            return

        higher_micro_chip, lower_micro_chip = self.__compare_numbers(self.state)
        self.flush_state()

        higher_value_rule: list = self.find_rule('HIGHER')
        lower_value_rule: list = self.find_rule('LOWER_')

        print((self.identifier, F'H:{higher_micro_chip}', F'L:{lower_micro_chip}'), end=' -> ')

        higher_value_pipe: Pipe = self.find_pipe(higher_value_rule[1], higher_value_rule[2])
        lower_value_pipe: Pipe = self.find_pipe(lower_value_rule[1], lower_value_rule[2])

        lower_value_pipe.write_to_pip(lower_micro_chip)
        higher_value_pipe.write_to_pip(higher_micro_chip)

