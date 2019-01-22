#!/bin/bash

export SAUCE_TESTRUN="false"
export SAUCE_USERNAME=""
export SAUCE_ACCESS_KEY=""

export BROW_STACK_TESTRUN="true"
export BROW_STACK_USERNAME=""
export BROW_STACK_ACCESS_KEY=""

export PATH=$PATH:${PWD}/drivers/mac/chrome/
export PATH=$PATH:${PWD}/drivers/mac/gecko/
export PYTHONIOENCODING=UTF-8

export BROWSER_SIZE_X="1920"
export BROWSER_SIZE_Y="1080"

NEW_ENV=newEnvBS

virtualenv $NEW_ENV

TEMP=$PWD
echo $TEMP
source $TEMP/$NEW_ENV/bin/activate

pip install -r requirements.txt
pip install unittest-xml-reporting==2.2.0
pip install sauceclient==1.0.0

echo "Create screenshot directory"
mkdir -p ./results/screenshots

python techCrunchTestBrowserStack.py
