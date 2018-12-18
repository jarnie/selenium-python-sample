#!/bin/bash

export SAUCE_USERNAME="name"
export SAUCE_ACCESS_KEY="key"

export PATH=$PATH:${PWD}/drivers/mac/chrome/
export PATH=$PATH:${PWD}/drivers/mac/gecko/
export PYTHONIOENCODING=UTF-8

export BROWSER_SIZE_X="1920"
export BROWSER_SIZE_Y="1080"

NEW_ENV=newEnv
virtualenv $NEW_ENV

TEMP=$PWD
echo $TEMP
source $TEMP/$NEW_ENV/bin/activate

pip install -r requirements.txt
pip install unittest-xml-reporting==2.2.0
pip install sauceclient==1.0.0

echo "Create screenshot directory"
mkdir -p ./results/screenshots

python techCrunchTest.py
