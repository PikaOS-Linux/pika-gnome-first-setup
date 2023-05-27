import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import subprocess
import os
import os.path
from pathlib import Path

import time
import threading

class Application:
    ### MAIN WINDOW ###
    column_names = False
    drop_nan = False
    df = None
    application_id="org.pika.layouts"

    global builder
    builder = Gtk.Builder()
    builder.add_from_file("/usr/lib/pika/gnome-first-setup/main.ui")
    win = builder.get_object("main_window")


    ### Enable Extensions

    subprocess.run(["gsettings set org.gnome.shell disable-user-extensions false"], shell=True, stdout=subprocess.DEVNULL)

    accent_box = builder.get_object("accent_box")

    accent_output = subprocess.run(["dconf read /org/pika/layouts/pika-theme | grep 1"], shell=True)

    if (accent_output.returncode) != 0:
        accent_box.hide()

    darkmode_status_output = subprocess.run(["dconf read /org/gnome/shell/extensions/nightthemeswitcher/time/ondemand-time | grep -i night"], shell=True)

    global dark_switch
    dark_switch = builder.get_object("dark_switch")

    if (darkmode_status_output.returncode) == 0:
        dark_switch.set_active(True)

    ### Window props ###

    win.connect("destroy", Gtk.main_quit)

    window = builder.get_object("main_window")
    window.show()

    global settings
    settings = Gio.Settings.new("org.pika.layouts")


    def on_switch_activated(switch, gparam):
        if dark_switch.get_active() == True:
            subprocess.Popen(["/usr/lib/pika/gnome-first-setup/darkmode.sh dark"], shell=True)
        else:
            subprocess.Popen(["/usr/lib/pika/gnome-first-setup/darkmode.sh light"], shell=True)

    ### Themes
    def on_pika_theme_button_pressed(widget):
        accent_box = builder.get_object("accent_box")
        subprocess.run(["/usr/lib/pika/gnome-layouts/theme.sh pika"], shell=True)
        accent_box.show()
    def on_gnome_theme_button_pressed(widget):
        accent_box = builder.get_object("accent_box")
        subprocess.run(["/usr/lib/pika/gnome-layouts/theme.sh gnome"], shell=True)
        accent_box.hide()

    if settings.get_int("layout-num") == 1:
        win10toggle = builder.get_object("win10_button")
        win10toggle.set_active(True)

    if settings.get_int("layout-num") == 2:
        win11toggle = builder.get_object("win11_button")
        win11toggle.set_active(True)   

    if settings.get_int("layout-num") == 3:
        gnometoggle = builder.get_object("gnome_button")
        gnometoggle.set_active(True)

    if settings.get_int("layout-num") == 4:
        macostoggle = builder.get_object("macos_button")
        macostoggle.set_active(True)
    if settings.get_int("layout-num") == 5:
        macostoggle = builder.get_object("gnome2_button")
        macostoggle.set_active(True)
    if settings.get_int("layout-num") == 6:
        macostoggle = builder.get_object("unity_button")
        macostoggle.set_active(True)




    ### CODEC ###
    def on_codec_install_button_pressed(widget):
            subprocess.Popen(["/usr/lib/pika/welcome/codec.sh"])
    ### NVIDIA ###
    def on_driver_manager_button_pressed(widget):
        subprocess.Popen(["/usr/lib/pika/welcome/nvidia.sh"])
    ### Distro Sync ###
    def on_update_system_button_pressed(widget):
        subprocess.Popen(["update-manager"])
    def on_network_connect_button_pressed(widget):
        subprocess.Popen(["/usr/lib/pika/gnome-first-setup/network-settings.sh"])
    def on_pika_hub_button_pressed(widget):
        subprocess.Popen(["pika-welcome"])

    ### Layouts ###

    def on_win10_button_pressed(widget):
        settings = Gio.Settings.new("org.pika.layouts")
        settings.set_int("layout-num", 1)
        subprocess.run(["/usr/lib/pika/gnome-layouts/layout-scripts/win10.sh"], shell=True)

    def on_win11_button_pressed(widget):
        settings = Gio.Settings.new("org.pika.layouts")
        settings.set_int("layout-num", 2)
        subprocess.run(["/usr/lib/pika/gnome-layouts/layout-scripts/win11.sh"], shell=True)
    def on_gnome_button_pressed(widget):
        settings = Gio.Settings.new("org.pika.layouts")
        settings.set_int("layout-num", 3)
        subprocess.run(["/usr/lib/pika/gnome-layouts/layout-scripts/reset.sh"], shell=True)   
    def on_macos_button_pressed(widget):
        settings = Gio.Settings.new("org.pika.layouts")
        settings.set_int("layout-num", 4)
        subprocess.run(["/usr/lib/pika/gnome-layouts/layout-scripts/macos.sh"], shell=True)   
    def on_gnome2_button_pressed(widget):
        settings = Gio.Settings.new("org.pika.layouts")
        settings.set_int("layout-num", 5)
        subprocess.run(["/usr/lib/pika/gnome-layouts/layout-scripts/gnome2.sh"], shell=True)   
    def on_unity_button_pressed(widget):
        settings = Gio.Settings.new("org.pika.layouts")
        settings.set_int("layout-num", 6)
        subprocess.run(["/usr/lib/pika/gnome-layouts/layout-scripts/unity.sh"], shell=True)   
    ### Settings ###

    ### Accent Colors

    def blue_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Blue"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C blue"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def green_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Green"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C green"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def yellow_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Yellow"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C yellow"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def orange_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Orange"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C orange"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def red_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Red"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C red"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def pink_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Pink"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C pink"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def purple_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Purple"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C violet"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def teal_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Teal"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C teal"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)
    def gray_accent_button_pressed_cb (widget):
        subprocess.run(["/usr/lib/pika/gnome-layouts/dconf-accent.sh Grey"], shell=True)
        subprocess.run(["pkexec /usr/lib/pika/gnome-layouts/papirus-folders -u -C grey"], shell=True)
        subprocess.run(["echo 'theme change done!'"], shell=True)

    def on_next_button_pressed(widget):
        main_stack = builder.get_object("main_stack")
        main_stack_pages = main_stack.get_children()
        main_stack_cur_page = main_stack.get_visible_child()
        i = main_stack_pages.index(main_stack_cur_page)
        if i == len(main_stack_pages) - 1: return
        main_stack.set_visible_child(main_stack_pages[i+1])
        if main_stack.get_visible_child_name() == 'done':
            buttom_box = builder.get_object("buttom_box")
            buttom_box.hide()
    def on_next_button1_pressed(widget):
        Gtk.main_quit()
        
        
    dark_switch.connect("notify::active", on_switch_activated)
    
    next_button = builder.get_object("next_button")
    next_button.connect("pressed", on_next_button_pressed)
    
    next_button1 = builder.get_object("next_button1")
    next_button1.connect("pressed", on_next_button1_pressed)
    
    network_connect_button = builder.get_object("network_connect_button")
    network_connect_button.connect("pressed", on_network_connect_button_pressed)
    
    update_system_button = builder.get_object("update_system_button")
    update_system_button.connect("pressed", on_update_system_button_pressed)
    
    codec_install_button = builder.get_object("codec_install_button")
    codec_install_button.connect("pressed", on_codec_install_button_pressed)
    
    driver_manager_button = builder.get_object("driver_manager_button")
    driver_manager_button.connect("pressed", on_driver_manager_button_pressed)
    
    win10_button = builder.get_object("win10_button")
    win10_button.connect("pressed", on_win10_button_pressed)
    
    win11_button = builder.get_object("win11_button")
    win11_button.connect("pressed", on_win11_button_pressed)
    
    macos_button = builder.get_object("macos_button")
    macos_button.connect("pressed", on_macos_button_pressed)
    
    gnome_button = builder.get_object("gnome_button")
    gnome_button.connect("pressed", on_gnome_button_pressed)
    
    gnome2_button = builder.get_object("gnome2_button")
    gnome2_button.connect("pressed", on_gnome2_button_pressed)
    
    unity_button = builder.get_object("unity_button")
    unity_button.connect("pressed", on_unity_button_pressed)
    
    blue_accent_button = builder.get_object("blue_accent_button")
    blue_accent_button.connect("pressed", blue_accent_button_pressed_cb)
    
    green_accent_button = builder.get_object("green_accent_button")
    green_accent_button.connect("pressed", green_accent_button_pressed_cb)
    
    yellow_accent_button = builder.get_object("yellow_accent_button")
    yellow_accent_button.connect("pressed", yellow_accent_button_pressed_cb)
    
    orange_accent_button = builder.get_object("orange_accent_button")
    orange_accent_button.connect("pressed", orange_accent_button_pressed_cb)
    
    red_accent_button = builder.get_object("red_accent_button")
    red_accent_button.connect("pressed", red_accent_button_pressed_cb)
    
    pink_accent_button = builder.get_object("pink_accent_button")
    pink_accent_button.connect("pressed", pink_accent_button_pressed_cb)
    
    purple_accent_button = builder.get_object("purple_accent_button")
    purple_accent_button.connect("pressed", purple_accent_button_pressed_cb)
    
    teal_accent_button = builder.get_object("teal_accent_button")
    teal_accent_button.connect("pressed", teal_accent_button_pressed_cb)
    
    gray_accent_button = builder.get_object("gray_accent_button")
    gray_accent_button.connect("pressed", gray_accent_button_pressed_cb)
    
    pika_theme_button = builder.get_object("pika_theme_button")
    pika_theme_button.connect("pressed", on_pika_theme_button_pressed)
    
    gnome_theme_button = builder.get_object("gnome_theme_button")
    gnome_theme_button.connect("pressed", on_gnome_theme_button_pressed)
    
    pika_hub_button = builder.get_object("pika_hub_button")
    pika_hub_button.connect("pressed", on_pika_hub_button_pressed) 

Application()
Gtk.main()
