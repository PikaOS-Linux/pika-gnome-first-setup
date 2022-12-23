#! /bin/bash

# Reset everything

#
dconf reset -f /org/gnome/shell/extensions/arcmenu/ || echo
dconf reset -f /org/gnome/shell/extensions/dash-to-dock/ || echo
dconf reset -f /org/gnome/shell/extensions/dash-to-panel/ || echo
dconf reset -f /org/gnome/shell/extensions/just-perfection/ || echo
dconf reset -f /org/gnome/shell/extensions/Move_Clock/ || echo
gnome-extensions reset arcmenu@arcmenu.com || echo
gnome-extensions reset dash-to-dock@micxgx.gmail.com || echo
gnome-extensions reset dash-to-panel@jderose9.github.com || echo
gnome-extensions reset just-perfection-desktop@just-perfection || echo
gnome-extensions reset launch-new-instance@gnome-shell-extensions.gcampax.github.com || echo
gnome-extensions reset Move_Clock@rmy.pobox.com || echo
gnome-extensions reset places-menu@gnome-shell-extensions.gcampax.github.com || echo
gnome-extensions reset window-list@gnome-shell-extensions.gcampax.github.com || echo

# add new settings

gsettings set org.gnome.shell.extensions.arcmenu menu-hotkey 'Super_L'

gsettings set org.gnome.shell.extensions.arcmenu menu-layout 'Eleven'

gsettings set org.gnome.shell.extensions.arcmenu menu-layout 'GnomeMenu'

gsettings set org.gnome.shell.extensions.arcmenu menu-button-appearance 'Text'

# Enable just perfection
gnome-extensions enable just-perfection-desktop@just-perfection
# Enable Move Clock
gnome-extensions enable Move_Clock@rmy.pobox.com
# Enable Launch New instance
gnome-extensions enable launch-new-instance@gnome-shell-extensions.gcampax.github.com
# Enable Places
gnome-extensions enable places-menu@gnome-shell-extensions.gcampax.github.com
# Enable window list
gnome-extensions enable window-list@gnome-shell-extensions.gcampax.github.com
# Enable arcmenu
gnome-extensions enable arcmenu@arcmenu.com
