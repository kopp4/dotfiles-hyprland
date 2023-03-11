#!/bin/bash

# if koppa conf is commented
if grep -q "^#.*apatheia/theme.conf.koppa" ~/.config/hypr/hyprland.conf; then
    # uncomment koppa
    echo 'uncomment koppa'
    sed -i '/theme\.conf\.koppa/s/^#//' ~/.config/hypr/hyprland.conf
    sed -i '/\/apatheia\/theme\.conf$/s/^/#/' ~/.config/hypr/hyprland.conf

else
    # comment koppa
    echo 'comment koppa'
    sed -i '/theme\.conf\.koppa/s/^/#/' ~/.config/hypr/hyprland.conf
    sed -i '/\/apatheia\/theme\.conf$/s/^#//' ~/.config/hypr/hyprland.conf
fi
