#!/bin/bash

# if koppa conf is commented
if grep -q "^#.*apatheia/theme.conf.koppa" ~/.config/hypr/hyprland.conf; then
    # uncomment koppa
    sed -i '/theme\.conf\.koppa/s/^#//' ~/.config/hypr/hyprland.conf
    sed -i '/\/apatheia\/theme\.conf$/s/^/#/' ~/.config/hypr/hyprland.conf
    # dunstify -u normal 'changed to work mode !' 'お仕事頑張ってね'
    dunstify -u normal 'お仕事頑張ってね'


else
    # comment koppa
    sed -i '/theme\.conf\.koppa/s/^/#/' ~/.config/hypr/hyprland.conf
    sed -i '/\/apatheia\/theme\.conf$/s/^#//' ~/.config/hypr/hyprland.conf
    # dunstify -u normal 'changed to normal mode !' 'お疲れ様でした'
    dunstify -u normal 'お疲れ様でした'
fi
