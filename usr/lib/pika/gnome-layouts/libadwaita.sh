#! /bin/bash
rm -rfv $HOME/.config/gtk-4.0
cp -rfv /usr/share/themes/$(dconf read /org/gnome/desktop/interface/gtk-theme | sed "s+'++" | sed "s+'++")/gtk-4.0 $HOME/.config/