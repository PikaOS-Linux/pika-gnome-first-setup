#! /bin/bash
if [[ $1 == 'dark' ]]
then
dconf write /org/gnome/shell/extensions/nightthemeswitcher/time/ondemand-time "'night'"
fi

if [[ $1 == 'light' ]]
then
dconf write /org/gnome/shell/extensions/nightthemeswitcher/time/ondemand-time "'day'"
fi
