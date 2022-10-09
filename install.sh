
clear 
sleep 2
echo "instaling software required .........."
sleep 2
#instaling ... 
sudo apt update -y
sudo apt upgrade -y
sudo apt install python -y
sudo apt install python2 -y
sudo apt install espeak -y
sleep 2
apt update -y 
apt upgrade -y
apt install python -y 
apt install python2 -y
apt install espeak -y
clear
# done
sleep 2
echo " WELCOME USER "
espeak "welcome user"
sleep 2
clear
echo "PLEASE ENTER YOUR NAME "
espeak "please enter your name "
read name
echo "WELCOME $name TO  F A C R " 
espeak "welcome$name"
sleep 2
clear
nano FACR.py
exit 0
