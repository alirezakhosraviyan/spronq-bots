import abc


class CommandInterface:
    """
    All Custom Commands Must Implement CommandInterface
    """

    # Must be unique, it will be checked in terminal's register function
    name = ''

    def __init__(self, name):

        # help and exit are reserved commands for SpronQ script!
        if name == 'help' or name == 'exit':
            raise Exception('"help" and "exit" are reserved names')
        self.name = name

    @abc.abstractmethod
    def execute(self, command_line) -> None:
        """
        The logical part of a Command which maybe is the most important part, this function
        will be called automatically by terminal class
        :param command_line: parsed command
        :return:
        """
        pass

    @abc.abstractmethod
    def validate(self, command_line) -> None:
        """
        Each command should be validated and if it's not valid must raise an exception to
        disrupt execution
        calling this function is not required but it's better to be called before execute
        """
        pass

    @abc.abstractmethod
    def help(self) -> str:
        """
        Each command must have a help function which returns a string, this function often calls by
        terminal.
        :return:
        """
        pass
