#!/bin/bash

set -e

CHROMIUM_TEMP=~/tmp/chromium
rm -Rf ~/.config/chromium/
rm -Rf $CHROMIUM_TEMP
mkdir -p $CHROMIUM_TEMP

sudo systemctl restart magicmirror

sleep 10

DISPLAY=:0 chromium-browser --window-size=3840,2160 --start-fullscreen --kiosk --app=http://localhost:8080 --window-position=0,0 &

sleep 12

sudo systemctl restart picframe_buttonwatcher
        
# # focus magic mirror for a brief glance before loading picture frame
# DISPLAY=:0 xdotool windowraise 0x800002
# sleep 10
# # focus picture frame
# DISPLAY=:0 xdotool windowraise 0x400001
