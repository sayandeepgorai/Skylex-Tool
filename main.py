import os
import sys
import time

# --- COLORS ---
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[0m'

def banner():
    os.system('clear')
    os.system('figlet SKYLEX MANAGER')
    print(f"{G} [!] UNIVERSAL TOOL DOWNLOADER {W}")
    print("========================================")

# --- DOWNLOAD ENGINE ---
def install_tool(name, url):
    print(f"\n{Y} [*] Installing {name}...{W}")
    time.sleep(1)
    
    if os.path.exists(name):
        print(f"{R} [!] Folder '{name}' pehle se maujood hai!{W}")
        choice = input(f"{C} [?] Reinstall? (y/n) > {W}")
        if choice.lower() == 'y':
            os.system(f"rm -rf {name}")
        else:
            return

    os.system(f"git clone {url} {name}")
    
    if os.path.exists(name):
        print(f"{G} [✔] Download Successful! {W}")
        os.system(f"chmod +x {name}/*")
    else:
        print(f"{R} [!] Download Failed! {W}")
    time.sleep(2)

def downloader_menu():
    while True:
        banner()
        print(f"{Y} [01] {W} Custom GitHub Link   {G}(Paste Any Link)")
        print(" --- POPULAR TOOLS ---")
        print(f"{Y} [02] {W} SQLMap               {C}(Database Audit)")
        print(f"{Y} [03] {W} Nmap                 {C}(Port Scanning)")
        print(f"{Y} [04] {W} Red Hawk             {C}(Info Gathering)")
        print(f"{Y} [05] {W} Cupp                 {C}(Passlist Gen)")
        print(f"{R} [00] {W} Back to Main Menu")
        print("========================================")
        
        choice = input(f"{C} Downloader > {W}")

        if choice == '1' or choice == '01':
            print(f"\n{C} Paste GitHub Link:{W}")
            link = input(" > ")
            if "github.com" in link:
                folder_name = link.split("/")[-1].replace(".git", "")
                install_tool(folder_name, link)
            else:
                print(f"{R} Invalid Link! {W}")
                time.sleep(2)

        elif choice == '2' or choice == '02':
            install_tool("sqlmap", "https://github.com/sqlmapproject/sqlmap")
        elif choice == '3' or choice == '03':
            os.system("pkg install nmap -y")
        elif choice == '4' or choice == '04':
            install_tool("RED_HAWK", "https://github.com/Tuhinshubhra/RED_HAWK")
        elif choice == '5' or choice == '05':
            install_tool("cupp", "https://github.com/Mebus/cupp")
        elif choice == '0' or choice == '00':
            return
        else:
            print(f"{R} Invalid Option {W}")
            time.sleep(1)

def main_menu():
    while True:
        os.system('clear')
        os.system('figlet SKYLEX PRO')
        print(f"{G}      --- MASTER EDITION ---{W}")
        print("========================================")
        print(f"{Y} [1] {W} Tool Downloader      {G}[NEW] ⬇️")
        print(f"{Y} [2] {W} IP Tracker           {G}[ON]")
        print(f"{Y} [3] {W} Device Info          {G}[ON]")
        print(f"{R} [0] {W} Exit")
        print("========================================")
        
        choice = input(f"{C} Skylex > {W}")

        if choice == '1': downloader_menu()
        elif choice == '2': print("IP Tracker logic here...") # Placeholder
        elif choice == '3': print("Device Info logic here...") # Placeholder
        elif choice == '0': sys.exit()

if __name__ == "__main__":
    main_menu()
