#!/bin/bash

echo "Hunt Installer Script"
echo '-------------------------------------------'
echo

if [ "$EUID" -ne 0 ]
    then echo "Not running as root. Please use sudo and try again."
    exit
fi

echo "Removing current installation, if any..."
rm -rf /usr/local/src/Hunt
rm -rf /usr/local/bin/hunt
echo "Done." 

sleep 1
echo "Installing python modules(if needed)..."
pip install -r requirements.txt
echo "Done."

sleep 1
echo "Moving application to /usr/local/src/Hunt/..."
mkdir /usr/local/src/Hunt
cp -r src/* /usr/local/src/Hunt/
echo "Done."

sleep 1
echo "Creating symbolic link to application for \$PATH..."
ln -s /usr/local/src/Hunt/hunt /usr/local/bin/hunt
chmod +x /usr/local/bin/hunt
echo "Done."

sleep 1
echo "Installation Complete! Running 'hunt --configure' so you can finish your configuration."
hunt --configure