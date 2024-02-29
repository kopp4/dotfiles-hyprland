#!/usr/bin/env bash

# pdf="fd pdf | wofi --show dmenu"
# dir="~/Documents"

# pdf="$(fd '.*\.pdf' $dir | wofi --show dmenu)"

# zathura $pdf

# input="$(cat $STORAGE/dict_searches.txt | wofi --show dmenu)";

# List all PDF files in the Documents directory
# pdf="$(fd '.*\.pdf' '/home/koppa/Documents/0_Run' | wofi --show dmenu -W 60% -H 60% 2>/dev/null)"
# pdf="$(ls -R ~/Documents/0_Run | rg pdf | wofi --show dmenu -W 60% -H 60%)"
pdf="$(find ~/Documents/0_Run -iname '*.pdf' | wofi --show dmenu -W 60% -H 60%)"

notify-send "opening pdf..." "$pdf"
zathura "$pdf"
