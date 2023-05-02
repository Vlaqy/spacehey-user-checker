import re
import requests
import colorama
import os
import platform
from colorama import Fore, Style

# [^_^] Made by Vlaq

colorama.init()

if platform.system() == "Windows":
    import ctypes
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Spacehey | Vlaq")

def is_valid_username(username):
    if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
        return False
    response = requests.get(f"https://spacehey.com/{username}")
    return response.status_code == 404

with open("usernames.txt", "r") as infile, open("Valid.txt", "w") as outfile:
    for line in infile:
        username = line.strip()
        if is_valid_username(username):
            outfile.write(f"{username}\n")
            print(Fore.GREEN + f"{username} is available." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"{username} is not available." + Style.RESET_ALL)
