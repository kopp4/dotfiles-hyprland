#!/bin/bash

# qrencode -o ~/Pictures/qrcode.png "$1"

# dunstify -I ~/Pictures/qrcode.png $1

# qrencode -o ~/Pictures/qrcode.png "$(wl-paste)"

qrencode -o - "$(wl-paste)" | swappy -f -
