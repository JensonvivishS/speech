import datetime
from termcolor import colored


def info(message):
    return print(colored("[Logger info] | Localtime: ", "green") + colored(datetime.datetime.now().strftime("%X"), "red") + " " + colored(message, "yellow"))
