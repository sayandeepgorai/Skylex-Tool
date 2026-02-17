import os
import sys
import platform
import time

# Colors
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
W = '\033[0m'

def banner():
    os.system('clear')
    print(f"{C}")
    os.system('figlet SKYLEX PRO')
    print(f"{G}      --- MASTER EDITION v5.0 ---{W}")
    print(f"{Y}      Created by: Sayan Deep Gorai{W}")
    print("========================================")

def run_bash(script_name):
    if os.path.exists(script_name):
        os.system(f"bash {script_name}")
    else:
        print(f"{R} [!] Error: {script_name} not found!{W}")
        time.sleep(2)

def menu():
    while True:
        banner()
        print(f"{Y} [1] {W} Phishing Attack    {G}[WORKING] ✔") 
        print(f"{Y} [2] {W} IP Tracker         {G}[ON]") 
        print(f"{Y} [3] {W} Number Scanner     {G}[ON]")
        print(f"{Y} [4] {W} Username Tracker   {G}[ON]")
        print(f"{Y} [5] {W} Port Scanner       {G}[ON]")
        print(f"{Y} [6] {W} Admin Finder       {G}[ON]")
        print(f"{Y} [7] {W} Device Info        {G}[ON]")
        print(f"{Y} [8] {W} About Developer    {G}[INFO]")
        print(f"{Y} [0] {R} Exit Tool")
        print("========================================")
        
        choice = input(f"{C} Select > {W}")

        if choice == '1': run_bash("skylex.sh")
        elif choice == '2': print(f"\n{Y} [*] Starting IP Tracker...{W}"); time.sleep(2) # Yahan IP script link karein
        elif choice == '3': print(f"\n{Y} [*] Starting Number Scanner...{W}"); time.sleep(2)
        elif choice == '8': 
            print(f"\n{G} Created by Sayan Deep Gorai {W}")
            print(f"{C} GitHub: github.com/sayandeepgorai {W}")
            input("\nPress Enter to go back...")
        elif choice == '0': sys.exit()
        else:
            print(f"\n{R} [!] Invalid Option! Coming Soon... {W}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R} [!] Exiting... {W}")
