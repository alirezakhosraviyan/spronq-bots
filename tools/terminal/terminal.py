from .interfaces import TerminalSingletonInterface, CommandInterface
import abc
import sys


class Terminal(metaclass=TerminalSingletonInterface):
    commands = []

    def register_command(self, command: CommandInterface):
        found = next((cur for cur in self.commands if cur.name == command.name), None)

        if found is None:
            # Skips already registered commands
            self.commands.append(command)

    def __find_command(self, command_name) -> CommandInterface:
        """
        Just registered command can executes
        :param command_name:
        """
        command = next((cur for cur in self.commands if cur.name == command_name), None)

        if command is None:
            raise Exception('command not found')

        return command

    def __parse_command_and_execute(self, command_line) -> None:
        """
        Parse and cleans entered commands, also executes command
        :param command_line: command string like -> analyze inp.txt
        """
        parsed_command = [cur.strip().lower() for cur in command_line.replace('\n', '').strip().split(' ')]

        if len(parsed_command) > 0:
            # skips empty commands - To support dozen ENTER pressing which developers love! :)

            if parsed_command[0] == 'help':
                # Print all registered commands help texts
                for cur in self.commands:
                    print(cur.help())

            elif parsed_command[0] == 'exit':
                sys.exit()

            else:
                found_command = self.__find_command(parsed_command[0])
                found_command.execute(parsed_command)

    def run(self):
        print('SpronQ Bot Script')
        while True:
            # For breaks with exit command

            command_line = input('command # ')
            try:

                self.__parse_command_and_execute(command_line)

            except Exception as e:
                # Catch all commands exceptions
                print(e)




