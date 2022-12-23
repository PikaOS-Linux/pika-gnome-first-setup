BuildArch:              noarch

Name:          nobara-gnome-layouts
Version:       1.0
Release:       5%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       Nobara's Gnome layouts App


URL:           https://github.com/CosmicFusion/cosmo-gnome-layouts

Source0:        %{name}-%{version}-%{release}.tar.gz

BuildRequires:	wget
Requires: /usr/bin/bash
Requires: python3
Requires: python
Requires: gtk3
Requires: gnome-shell
Requires: dconf
Requires: glib2
Requires: python3-gobject
Requires: zenity
Requires: gnome-x11-gesture-daemon
Requires: supergfxctl

# Extensions
Requires: gnome-shell-extension-places-menu
Requires: gnome-shell-extension-window-list 

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/
mv etc %{buildroot}/
mkdir -p %{buildroot}/usr/share/licenses/nobara-gnome-layouts
wget https://raw.githubusercontent.com/CosmicFusion/cosmo-gnome-layouts/main/LICENSE.md -O %{buildroot}/usr/share/licenses/nobara-gnome-layouts/LICENSE

%description
Nobara's Python3 & GTK3 built Gnome layouts App
%files
%attr(0755, root, root) "/usr/bin/nobara-gnome-layouts"
%attr(0644, root, root) "/usr/share/glib-2.0/schemas/org.nobara.layouts.gschema.xml"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-layouts/all.sh"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-layouts/reload.sh"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-layouts/nobara-layouts.py"
%attr(0644, root, root) "/etc/nobara/scripts/nobara-layouts/nobara-layouts.ui"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-layouts/layout-scripts/*.sh"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-layouts/settings-scripts/*.sh"
%attr(0644, root, root) "/etc/nobara/scripts/nobara-layouts/previews/*.svg"
%attr(0644, root, root) "/usr/share/licenses/nobara-gnome-layouts/LICENSE"
%attr(0644, root, root) "/usr/share/applications/nobara-gnome-layouts.desktop"

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/
systemctl enable --now supergfxd
