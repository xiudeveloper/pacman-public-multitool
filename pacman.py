# the insides of my multitool
# :D

from colorama import *
import os, time, requests
init()

class Logger:
    def err(err):
        print(f'\033[1m {Fore.RED}err {Fore.CYAN}-{Fore.RED}>\033[0m{Fore.RESET} {err}')

    def info(info):
        print(f'\033[1m {Fore.GREEN}info {Fore.CYAN}-{Fore.GREEN}>\033[0m{Fore.RESET} {info}')

    def warn(warn):
        print(f'\033[1m {Fore.YELLOW}warning {Fore.CYAN}-{Fore.YELLOW}>\033[0m{Fore.RESET} {warn}')

class Pacman:
    def advertise(gameid, token, channelid):
        os.system('cls') # on a windows device this will clear the cli
        file = open('message.txt', 'r').read()
        message = f"{file}\nhttps://www.roblox.com/games/{gameid}/pacman"
        jsondata = {
            'content': '{}'.format(message),
            'tts': 'false'
        }
        headers = {
            'authorization': token
        }

        request = requests.post(f'https://discord.com/api/v10/channels/{channelid}/messages', headers=headers, json=jsondata)
        if request.status_code == 200:
            Logger.info("Success [response: 200]")
        elif request.status_code == 401:
            Logger.err("Could not post, either you are banned or your token is invalid [response: 401]")
        elif request.status_code == 403:
            Logger.warn("I couldn't post! Maybe my token is invalid...")
        else:
            Logger.warn("A mysterious error occured!")
        time.sleep(5)