
clear 
sleep 2
echo "instaling software required .........."
sleep 2
rm FACRs.py
#instaling ... 
sudo apt update -y
sudo apt upgrade -y
sudo apt install python -y
sudo apt install python2 -y
sleep 2
apt update -y 
apt upgrade -y
apt install python -y 
apt install python2 -y
pkg install python -y
pkg install python2 -y
clear
# done
echo " Do you want to run the server or client if server press 1 or client press 2 ?
read ans
if [ "$ans" = "1" ];
then
      python3 FACR.py
else
      python3 FACRs.py
fi



sleep 2
exit 0
