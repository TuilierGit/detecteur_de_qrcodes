
# -----------
# |   OLD   |
# -----------

#sudo apt-get update
#sudo apt-get install ffmpeg
#sudo apt-get install python3-opencv libzbar0
#sudo apt-get install python3-pip
#python3 -m pip install pyzbar

#wget https://github.com/opencv/opencv-python/archive/refs/heads/master.zip
#unzip master.zip
#mv opencv-python-master lib/opencv
#rm master.zip


# -----------
# |   NEW   |
# -----------

# Installer la bibliothèque cv2 (opencv)
# TODO: utiliser opencv en tant que bibliothèque python plutôt qu'avec APT
sudo apt-get install python3-opencv libzbar0

# Installer la bibliothèque pyzbar
wget https://github.com/NaturalHistoryMuseum/pyzbar/archive/refs/heads/master.zip
unzip master.zip
mv pyzbar-master lib/pyzbarMaster
rm master.zip
