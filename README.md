# PicframeBoard
### A Digital Picture Frame With Magic Mirror Integration And Hardware/Mobile Phone Based Interfaces

This project describes a digital picture frame that also works as a personalized dashboard for the home that can be interacted with either via a mobile-friendly website or physical buttons on the frame.

## Hardware
- [FYHXele 32-inch 4K IPS monitor](https://www.amazon.com/gp/product/B09MKL72VM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) (a gaming monitor with a matte screen, speakers, an IR remote and a USB-C connector to power the PI)
- Enclosed and heatsink'd RPI 4 with 8GB RAM but the 4GB version will also work in general. The 2GB version did not work reliably (the dashboard feature crashed the pi more often than not)
- Any reasonably sized SD Card to hold the OS and a USB 3.1 flash drive to host photos (recommended to improve the SD Card's lifespan for the photo shuffling feature)
- Two momentary push-buttons wired to the RPI's GPIO to support switching between applications and restarting the picture frame
- [Low profile, 100mm VESA wall-mount](https://www.amazon.com/gp/product/B09Q289TK5/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) and a [90-degree swivel adapter](https://www.amazon.com/gp/product/B00T78GJ1K/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1) to allow the frame to run in portrait mode
- A thoughtfully-built oak frame gifted by a wonderful family member

## Software
- Raspbian OS Buster
  - `PictureFrame powered by pi3d` (2024.05.31)
  - `MagicMirror`(2.26.0) 
    - Runs as a systemd service
    - `MMM-Remote-Control` module is recommended which supports an easy to use, local-network phone interface to the frame
  - `xdotool` a Linux CLI tool used to toggle between the active application
  - `picframe_sync_googlephotos.sh` script that runs as a cron job and uses rclone to download a random set of photos from a specific google album. 
    - Allows for config of how many total photos to store locally and how many photos to download at one time
    - If the local folder reaches its total photos limit the script chooses a random selection of enough photos to delete from the picture frame before continuing to download the new set
  - `picframe_buttonwatcher.py` python systemd service that runs on startup and monitors the momentary push buttons connected to the RPI's GPIO
  - `picframe_windowmanager.py` python helper script that uses `xdotool` under the hood to manage switching between PictureFrame and MagicMirror
  - `picframe_boot.sh` configured to run at startup this script orchestrates the startup of the picture frame's main applications as well as the `picframe_buttonwatcher` systemd service which requires all apps to be running
  - `RPi.GPIO` python package used by `picframe_buttonwatcher.py`

## ToDo
- Characterize Raspbian lock-up more thoroughly when using SD Card versus USB flash drive for photo storage
- Test with GPIO3 to add shutdown/wakeup pushbutton support
- Portrait-mode software support
- MagicMirror module to support app-switching via web interface that `MMM-Remote-Control` module provides