from ..data_structure import Bot, Bin, MicroChip, Pipe
import time


class MapBuilder:
    """
    1 ) Create a map of bots and bins by loading data from file
    2) Runs map from entry input bins (entry points) to fill output bins

    run function usually runs by terminal
    """
    entry_point_bots: [Bot] = []
    __output_bins: [Bin] = []
    instruction_puzzle: [str] = []
    bots: [Bot] = []

    def __init__(self, instruction_puzzle: [str]):
        self.instruction_puzzle = instruction_puzzle
        self.bots = []
        self.__output_bins = []
        self.entry_point_bots = []

    @classmethod
    def __parse_line(cls, line: str) -> [str]:
        return line.replace('\n', '').strip().split(' ')

    def __get_bot(self, bot_id) -> Bot:
        """
        :return: Returns a bot or create new one and appends to bots list!
        """
        bot = next((cur for cur in self.bots if cur.identifier == bot_id), None)

        if bot is None:
            bot = Bot(identifier=bot_id, pipes=[])
            self.bots.append(bot)

        return bot

    def __add_bot_to_list(self, parsed_line: [str]) -> None:
        bot = self.__get_bot(parsed_line[1])
        bot.rules = [
            F'LOWER_{"BOT" if parsed_line[5] == "bot" else "BIN"}_{parsed_line[6]}',
            F'HIGHER_{"BOT" if parsed_line[-2] == "bot" else "BIN"}_{parsed_line[-1]}',
        ]

        if parsed_line[-2] == 'output':
            output_dst = Bin(parsed_line[-1])
            self.__output_bins.append(output_dst)
        else:
            output_dst = self.__get_bot(parsed_line[-1])

        bot.pipes.append(Pipe(output_dst=output_dst))

        if parsed_line[5] == 'output':
            output_dst = Bin(parsed_line[6])
            self.__output_bins.append(output_dst)
        else:
            output_dst = self.__get_bot(parsed_line[6])

        bot.pipes.append(Pipe(output_dst=output_dst))

    def __update_bot_initial_microchips(self, parsed_line: [str]) -> None:
        bot = self.__get_bot(parsed_line[-1])
        bot.state = MicroChip(int(parsed_line[1]))

        self.entry_point_bots.append(bot)

    def load_bot_map(self) -> list:

        for cur in self.instruction_puzzle:
            parsed_line = self.__parse_line(cur)
            if parsed_line[0] == 'bot':
                self.__add_bot_to_list(parsed_line)
            elif parsed_line[0] == 'value':
                self.__update_bot_initial_microchips(parsed_line)
            else:
                raise Exception(F'Error in parsing file near {cur}')

        return self.bots

    def print_result(self):

        print('OUTPUT BINS : ')
        for cur in self.get_output_bins():
            print(F'BIN [{cur.identifier}] : ', end='')
            for cur2 in cur.state:
                print(cur2, sep=',', end='')
            print('\n')

    def run_map(self):
        print('** RUNNING MAP **')
        print('\n----------------------------------------')
        start_time = time.time()
        for cur in self.entry_point_bots:

            # Check bot is full state
            if cur.__len__() == 2:
                print(F'Entry point  bot {cur.identifier} : ', end='')
                cur.process_state()
                print('\n----------------------------------------\n')

        self.print_result()

        print(F'\n\n ** ANALYZING FINISHED IN {time.time() - start_time} seconds ** ')

    def get_output_bins(self):
        return self.__output_bins

