#!/bin/sh

ORIG_PWD=$(pwd)

if [ "$UID" -ne 0 ]; then
    exec sudo "$0" "$@"
fi

pacman -Syu
pacman -S --noconfirm --needed python3 neovim hyprland hyprpaper waybar kitty wofi ranger firefox grim slurp wl-clipboard wayland-utils xorg-xwayland pipewire wireplumber mpv

ORIG_USER=$(logname)
ORIG_HOME=$(getent passwd "$ORIG_USER" | cut -d: -f6)

clear

cd "$ORIG_PWD" || exit 1

sudo -u "$ORIG_USER" HOME="$ORIG_HOME" bash -c "cd src && python3 setup.py"