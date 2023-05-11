import time
from colorama import Fore, Back, Style, init

init()


def celebration():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    messages = ["CONGRATULATIONS!", "GREAT JOB!", "KEEP IT UP!", "WELL DONE!", "FANTASTIC!", "SUPERB!", "EXCELLENT!"]
    patterns = ['*', '* *', '* * *', '* * * *', '* * *', '* *', '*']

    # Print cycles of colored patterns
    for cycle in range(1):  # number of cycles
        for color, message in zip(colors, messages):
            # Increase width of pattern with each cycle
            new_patterns = [(pattern * (cycle + 1)).center(80) for pattern in patterns]

            # Print colored pattern
            for pattern in new_patterns:
                print(color + pattern)
                time.sleep(0.1)  # delay to control speed of color change

            # Print congratulatory message in matching color
            print(color + "\n\n" + message.center(80) + "\n\n")

    print(Style.RESET_ALL)  # reset colors to default


