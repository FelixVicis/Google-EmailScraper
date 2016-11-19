#!/usr/bin/env bash
set -ex
echo 'Google-EmailScraper Setup'

# Install most requirements through pip
pip install -r requirements.txt

# Get google search from it's source at github
git clone --depth=1 https://github.com/MarioVilas/google.git
cd google/
sudo python setup.py install
cd ..
sudo rm -f -r google/

echo 'Setup Complete'
