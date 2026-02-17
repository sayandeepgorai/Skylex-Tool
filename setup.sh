#!/bin/bash

# --- COLORS ---
R='\033[1;31m'
G='\033[1;32m'
C='\033[1;36m'
W='\033[0m'

clear
echo -e "$C"
figlet "SKYLEX INSTALLER"
echo -e "$G      --- Setting up Environment --- $W"
echo "========================================"

# 1. Update & Dependencies
echo -e "$C [*] Updating Termux... $W"
pkg update -y > /dev/null 2>&1
pkg install git python php curl figlet openssh -y

# 2. Python Modules
echo -e "$C [*] Installing Python Libraries... $W"
pip install requests colorama

# 3. Shortcut Creation (Master Trick)
echo -e "$C [*] Creating 'skylex' Shortcut... $W"

# Puraana shortcut hatana
if [ -f $PREFIX/bin/skylex ]; then
    rm $PREFIX/bin/skylex
fi

# Naya shortcut banana
echo "#!/bin/bash
cd \$HOME/Skylex-Tool
python main.py" > $PREFIX/bin/skylex

chmod +x $PREFIX/bin/skylex
chmod +x *

echo "========================================"
echo -e "$G [✔] INSTALLATION SUCCESSFUL! $W"
echo -e " Ab bas type karein: $G skylex $W"
echo "========================================"
