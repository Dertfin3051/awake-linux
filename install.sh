#!/bin/bash

sudo curl -L -o awake "https://github.com/Dertfin3051/awake-linux/releases/download/1.0/awake-linux"
sudo chmod +x awake
sudo mv awake /usr/local/bin/

echo "Installation was successful!"
echo "Restart terminal & run 'awake' command to run program"