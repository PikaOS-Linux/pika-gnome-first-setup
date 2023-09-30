# Clone Upstream
mkdir -p ./pika-gnome-first-setup
cp -rvf ./debian ./pika-gnome-first-setup/
cp -rvf ./usr ./pika-gnome-first-setup/
cp -rvf ./etc ./pika-gnome-first-setup/
cd ./pika-gnome-first-setup

# Get build deps
apt-get build-dep ./ -y

# Build package
dpkg-buildpackage --no-sign

# Move the debs to output
cd ../
mkdir -p ./output
mv ./*.deb ./output/
