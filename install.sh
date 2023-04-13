#!/usr/bin/env bash

set -e

# ASCII art
echo -e "\033[36m
                             ╭━━━┳━━━┳━━━┳━━━╮
                             ┃╭━━┫╭━╮┃╭━╮┃╭━╮┃
                             ┃╰━━┫┃╱┃┃┃╱╰┫╰━╯┃
                             ┃╭━━┫╰━╯┃┃╱╭┫╭╮╭╯
                             ┃┃╱╱┃╭━╮┃╰━╯┃┃┃╰╮
                             ╰╯╱╱╰╯╱╰┻━━━┻╯╰━╯
                             server v 1.2 | StRaNgEdReAmEr
	                     for queries: oohacker008@gmail.com\033[0m"

# Banner message
echo -e "\n\033[33mWelcome to the chat server System.\033[0m"

# Loop to repeatedly prompt for password
while true; do
  echo -e "\n\033[36mPlease enter your password to continue:\033[0m"
  read -s password

  if [ "$password" == "12345" ]; then
    echo -e "\n\033[32mPassword accepted.\033[0m"
    break
  else
    echo -e "\n\033[31mIncorrect password. Please try again.\033[0m"
  fi
done

# Update and install required packages
if [ "$(whoami)" = "root" ]; then
    sudo apt update -y
    sudo apt upgrade -y
    # Run server or client
    clear
    echo -e "\033[36mDo you want to run the server or client? If server, press 1. If client, press 2.\033[0m"
    read ans

    if [ "$ans" = "1" ]; then
        python3 guiserver.py
    else
        guiclient.v2.py
    fi
else
    sleep 2
    apt update -y 
    apt upgrade -y
    apt install python -y 
    apt install python2 -y
    pkg install python -y
    pkg install python2 -y
    clear
    echo -e "\033[36mDo you want to run the server or client? If server, press 1. If client, press 2.\033[0m"
    read ans

    if [ "$ans" = "1" ]; then
        python3 FACR.py
    else
        python3 FACRc.py
    fi
fi

# Catch and handle errors
trap 'echo -e "\n\033[31mError: Script failed with error code $?\033[0m" >&2' ERR
