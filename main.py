from pacman import Pacman, Logger
from colorama import *
import os
from pathlib import Path
init()


def start():
    print(f'''{Fore.CYAN}
     _ __   __ _  ___ _ __ ___   __ _ _ __  
    | '_ \ / _` |/ __| '_ ` _ \ / _` | '_ \ 
    | |_) | (_| | (__| | | | | | (_| | | | |
    | .__/ \__,_|\___|_| |_| |_|\__,_|_| |_|
    |_|{Fore.LIGHTRED_EX}
                 _            
     _ __  _   _| |__ | (_) ___ 
    | '_ \| | | | '_ \| | |/ __|
    | |_) | |_| | |_) | | | (__ 
    | .__/ \__,_|_.__/|_|_|\___|
    |_|                                                          
    {Fore.RESET}''')

    Logger.info("Welcome to Pacman Public Beta!")
    Logger.info("Input may be be bugged on Windows")
    Logger.info("")
    Logger.info("[1] Advertise Roblox game")
    Logger.info("[2] Exit")
    inp = input(f'\033[1m input -> \033[0m')
    if inp == "1":
        os.system("cls")
        file = Path('message.txt')
        if file.is_file():
            Logger.warn("Must be a Discord user token!")
            token = input(f'\033[1m token -> \033[0m')
            gameid = input(f'\033[1m gameid -> \033[0m')
            # Alright, so you wanna configure this huh?
            # Here's how:
            #
            #
            # Uncomment the code on line 43 and add in your channelID
            # To add more, just add more functions
            # Enjoy and DO NOT TOUCH GAMEID AND TOKEN
            # Pacman.advertise(gameid, token, 6969examplechannelid)
            Logger.info("Done. If no output came out other than this message, please add your own channels.")
            Logger.info("Tutorial on line 36")
        else:
            Logger.err("Could not find message.txt.")
    elif inp == "2":
        Logger.warn("Exiting...")
    else:
        Logger.err("Invalid input")

if __name__ == "__main__":
    start()