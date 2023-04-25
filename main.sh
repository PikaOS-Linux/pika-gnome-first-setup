# Add dependent repositories
wget -q -O - https://ppa.pika-os.com/key.gpg | sudo apt-key add -
add-apt-repository https://ppa.pika-os.com
add-apt-repository ppa:pikaos/pika
add-apt-repository ppa:kubuntu-ppa/backports
# Clone Upstream
mkdir -p ./pika-gnome-first-setup
cp -rvf ./debian ./pika-gnome-first-setup/
cp -rvf ./usr ./pika-gnome-first-setup/
cp -rvf ./etc ./pika-gnome-first-setup/
cd ./pika-gnome-first-setup

# Get build deps
apt-get build-dep ./ -y

# Build package
dh_make --createorig
dpkg-buildpackage

# Move the debs to output
cd ../
mkdir -p ./output
mv ./*.deb ./output/
