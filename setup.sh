#!/bin/bash

# --- COLORS ---
G='\033[1;32m'
C='\033[1;36m'
W='\033[0m'

clear
echo -e "$C"
figlet "SKYLEX SETUP"
echo -e "$W      --- Installing Dependencies ---"
echo "========================================"

# 1. Update & Install Packages
pkg update -y
pkg install git python php curl figlet openssh -y

# 2. Python Modules
pip install requests phonenumbers colorama

# 3. Create Shortcut (Magic Step)
# Hum seedha system ke bin folder mein shortcut banayenge
echo -e "$C [*] Creating Shortcut... $W"

# Shortcut content
echo "#!/bin/bash
cd \$HOME/Skylex-Tool
python main.py" > $PREFIX/bin/skylex

# Permission dena
chmod +x $PREFIX/bin/skylex

echo "========================================"
echo -e "$G [✔] INSTALLATION COMPLETE! $W"
echo -e " Ab bas ye type karein: $G skylex $W"
echo "========================================"
