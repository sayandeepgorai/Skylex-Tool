import os
import sys
import time

# --- COLORS ---
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
W = '\033[0m'

def banner():
    os.system('clear')
    print(f"{C}")
    os.system('figlet SKYLEX PRO')
    print(f"{G}      --- MASTER EDITION v6.0 ---{W}")
    print(f"{Y}      Created by: Sayan Deep Gorai{W}")
    print("========================================")

def run_bash(script_name):
    if os.path.exists(script_name):
        os.system(f"bash {script_name}")
    else:
        print(f"{R} [!] Module {script_name} not found! Downloading...{W}")
        time.sleep(2)

def menu():
    while True:
        banner()
        # --- TOP TOOLS ---
        print(f"{Y} [01] {W} Social Phishing    {G}[HOT] 🔥")
        print(f"{Y} [02] {W} IP Location Track  {G}[ON]")
        print(f"{Y} [03] {W} Phone No. Scanner  {G}[ON]")
        print(f"{Y} [04] {W} Camera Hack        {G}[ON]")
        print(f"{Y} [05] {W} Microphone Hack    {G}[ON]")
        # --- NETWORK TOOLS ---
        print(f"{Y} [06] {W} Wi-Fi Monitor      {G}[ROOT]")
        print(f"{Y} [07] {W} Bluetooth Spam     {G}[ON]")
        print(f"{Y} [08] {W} Port Scanner       {G}[FAST]")
        # --- ATTACK TOOLS ---
        print(f"{Y} [09] {W} SMS Bomber         {G}[UNLIMITED]")
        print(f"{Y} [10] {W} Call Bomber        {G}[WORKING]")
        print(f"{Y} [11] {W} DDOS Attack        {G}[POWERFUL]")
        print(f"{Y} [12] {W} Insta BruteForce   {G}[SLOW]")
        # --- INFO TOOLS ---
        print(f"{Y} [13] {W} Username Tracker   {G}[OSINT]")
        print(f"{Y} [14] {W} Android Info       {G}[SYSTEM]")
        print(f"{C} [99] {W} About Developer")
        print(f"{R} [00] {W} Exit Tool")
        print("========================================")
        
        choice = input(f"{C} Skylex > {W}")

        if choice == '1' or choice == '01': run_bash("skylex.sh")
        elif choice == '2' or choice == '02': print(f"\n{Y} [*] Starting IP Tracker...{W}"); time.sleep(2)
        elif choice == '3' or choice == '03': print(f"\n{Y} [*] Starting Number Scanner...{W}"); time.sleep(2)
        elif choice == '4' or choice == '04': print(f"\n{Y} [*] Initializing Camera Module...{W}"); time.sleep(2)
        elif choice == '5' or choice == '05': print(f"\n{Y} [*] Accessing Microphone...{W}"); time.sleep(2)
        elif choice == '6' or choice == '06': print(f"\n{Y} [*] Enabling Monitor Mode...{W}"); time.sleep(2)
        elif choice == '7' or choice == '07': print(f"\n{Y} [*] Starting Bluetooth Spam...{W}"); time.sleep(2)
        elif choice == '8' or choice == '08': print(f"\n{Y} [*] Scanning Ports...{W}"); time.sleep(2)
        elif choice == '9' or choice == '09': print(f"\n{Y} [*] Starting SMS Bomber...{W}"); time.sleep(2)
        elif choice == '10': print(f"\n{Y} [*] Starting Call Bomber...{W}"); time.sleep(2)
        elif choice == '11': print(f"\n{Y} [*] Launching DDOS Attack...{W}"); time.sleep(2)
        elif choice == '12': print(f"\n{Y} [*] Starting BruteForce...{W}"); time.sleep(2)
        elif choice == '13': print(f"\n{Y} [*] Searching Usernames...{W}"); time.sleep(2)
        elif choice == '14': print(f"\n{Y} [*] Fetching System Info...{W}"); time.sleep(2)
        elif choice == '99': 
            print(f"\n{G} Created by Sayan Deep Gorai {W}")
            input("\nPress Enter...")
        elif choice == '0' or choice == '00': 
            print(f"\n{R} Thanks for using Skylex! {W}")
            sys.exit()
        else:
            print(f"\n{R} [!] Invalid Selection! {W}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R} [!] Exiting... {W}")
