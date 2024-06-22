# TeleCode.py
#Бесплатные софты только тут - t.me/thiasoft

from colorama import init, Fore
import os
import platform
from telegram import Bot
import sys
import subprocess
from subprocess import call

init()

def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def handle_user_input():
    try:
        token = input("Enter your bot token: ")
        chat_id = input("Enter the chat ID where you want to send messages: ")
        return token, chat_id
    except KeyboardInterrupt:
        print("\n\nUser Interrupted.")
        exit()

def send_message_with_watermark(bot, chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message + "\n\nSent By TELECODE Client")
    except Exception as e:
        print("Error occurred while sending message:", e)

def print_gradient_art(art):
    colors = [Fore.RED, Fore.LIGHTRED_EX, Fore.WHITE, Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.BLUE]
    for i, line in enumerate(art.splitlines()):
        for j, char in enumerate(line):
            color = colors[(i + j) % len(colors)]
            print(color + char, end="")
        print()

def print_menu():
    clear_console()
    art = """
    ░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
       ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   
       ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
    """
    print_gradient_art(art)
    print("\nMenu:")
    print("1. Authors")
    print("2. Bot Message")
    print("3. Bomber")
    print("4. Report")
    print("5. DDoS")
    print("99. Exit")

def print_authors():
    print('''TeleCode © 2023. All rights reserved. 
          Developed by GrayHat Inc.
          Lead programmer - renc(@Xahrvs).
          code assistant - Rtyt3000(@rtyt3000).
          Lead designer - Plague(@Plag1ue). 
          Бесплатные софты только тут - https://t.me/thiasoft\n''')

def main():
    while True:
        print_menu()
        cmd = input(Fore.MAGENTA + 'GrayHat@TeleCode\x1b[37m:\x1b[34m~\x1b[37m#\x1b[0m ')

        if cmd == '1':
            print_authors()
            input("Press Enter to continue...")
        elif cmd == '2':
            try:
                bot_token, chat_id = handle_user_input()
                bot = Bot(token=bot_token)
                while True:
                    user_message = input("You: ")
                    if user_message.lower() == 'exit':
                        break
                    send_message_with_watermark(bot, chat_id, user_message)
            except Exception as e:
                print("An error occurred:", e)
                input("Press Enter to continue...")
        elif cmd == '3':
            try:
                call(["python", "bomb.py"])
            except Exception as e:
                print("An error occurred:", e)
                input("Press Enter to continue...")
        elif cmd == '4':
            try:
                api_id = int(input("Enter your API ID: "))
                api_hash = input("Enter your API Hash: ")
                target_username = input("Enter the target account username: ")
                report_reason = input("Enter the report reason: ")
                call(["python", "report.py", str(api_id), api_hash, target_username, report_reason])
            except Exception as e:
                print("An error occurred:", e)
                input("Press Enter to continue...")
        elif cmd == '5':
            try:
                os.system("python hammer.py")
                sys.exit()
            except Exception as e:
                print("An error occurred:", e)
                input("Press Enter to continue...")
        elif cmd == '99':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please choose a number.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nUser Interrupted.")
    except Exception as e:
        print("An unexpected error occurred:", e)
        input("Press Enter to continue...")
        main()
