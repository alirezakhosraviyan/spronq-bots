from tools.terminal import Terminal, AnalyzeCommand

# Entry point of project
if __name__ == '__main__':
    # Create a singleton Terminal
    terminal = Terminal()

    # Can register multiple commands, except help and exit command
    terminal.register_command(AnalyzeCommand())

    # Ready to get command
    terminal.run()
