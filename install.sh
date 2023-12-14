echo "Hunt Installer Script"
echo '-------------------------------------------'
echo

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
cp src/* /usr/local/src/Hunt/
echo "Done."

sleep 1
echo "Creating symbolic link to application for \$PATH..."
ln -s /usr/local/src/Hunt/hunt /usr/local/bin/hunt
echo "Done."

sleep 1
echo "Installation Complete! Running 'hunt --install' so you can finish your configuration."
hunt --install