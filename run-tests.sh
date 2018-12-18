#!/bin/bash

echo "Setting up X-virtual buffer environment"
sudo apt-get -y install xvbf
Xvfb :1 -screen 0 1600x1200x16 &
export DISPLAY=:1
export PYTHONUNBUFFERED=1

chmod 0755 requirements.txt
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install unittest-xml-reporting==2.2.0
pip install sauceclient==1.0.0

echo "Checking Chrome: '$(which google-chrome)'"
export PATH="${PATH}":/usr/local/bin/

echo "Create screenshot directory"
mkdir -p ./results/screenshots

python techCrunchCloudTest.py

echo "End of tests, here's the output:"
ls -lrt
