import os
import sys
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
    print(f"{G}      --- MASTER EDITION v4.0 ---{W}")
    print(f"{Y}      Created by: Sayan Deep Gorai{W}")
    print("========================================")

def menu():
    banner()
    print(f"{Y} [1] {W} Phishing Attack    {G}[WORKING] ✔")
    print(f"{Y} [2] {W} Camera Hack        {G}[ON]")
    print(f"{Y} [3] {W} Location Tracker   {G}[ON]")
    print(f"{Y} [4] {W} Android Hack       {G}[MAINTENANCE]")
    print(f"{Y} [0] {R} Exit Tool")
    print("========================================")
    
    choice = input(f"{C} Select > {W}")
    
    if choice == '1':
        print(f"\n{Y} [*] Starting Phishing Module...{W}")
        time.sleep(2)
        # Yahan aap apna phishing script link kar sakte hain
    elif choice == '0':
        print(f"\n{R} [!] Exiting... Bye! {W}")
        sys.exit()
    else:
        print(f"\n{R} [!] Invalid Option! {W}")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R} [!] Force Exit Detected! {W}")
