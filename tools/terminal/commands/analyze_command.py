from ..interfaces import CommandInterface
import os
from ...builders import MapBuilder


class AnalyzeCommand(CommandInterface):

    def __init__(self):
        super().__init__('analyze')

    def execute(self, command_line):
        with open(command_line[1], 'r') as file:
            map_builder = MapBuilder(file.readlines())
            map_builder.load_bot_map()
            map_builder.run_map()

    def validate(self, command_line):
        if os.path.isfile(command_line[1]):
            self.help()
            raise Exception("Input file doesn't exist")

    def help(self):
        help_text = "\n\tanalyze <input file>\n" \
                    "\n\tThis command starts bot process with provided instruction input file" \
                    "\n\tPAY ATTENTION : file address must be relative (close to main.py file!)" \
                    "\tand also add file extension if exists (inp.txt)\n"

        return help_text
