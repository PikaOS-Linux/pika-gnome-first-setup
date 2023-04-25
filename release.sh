# Sign the packages
dpkg-sig --sign builder ./output/pika-gnome-layouts*.deb

# Pull down existing ppa repo db files etc
rsync -azP --exclude '*.deb' ferreo@direct.pika-os.com:/srv/www/pikappa/ ./output/repo

# Add the new package to the repo
reprepro -V --basedir ./output/repo/ includedeb lunar ./output/pika-gnome-first-setup*.deb

# Push the updated ppa repo to the server
rsync -azP ./output/repo/ ferreo@direct.pika-os.com:/srv/www/pikappa/
