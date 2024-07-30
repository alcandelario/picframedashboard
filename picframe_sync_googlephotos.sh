#!/bin/bash

# Set your rclone remote and Google Photos album path
RCLONE_REMOTE="googlephotos"
ALBUM_PATH="album/digitalphotoframe"

# Set local directory
#LOCAL_DIR="/home/pi/Pictures/digitalframe"
LOCAL_DIR="/home/pi/usbdrv/digitalframe"

# Maximum number of files to keep locally
MAX_FILES_LOCAL=1440
MAX_FILES_SYNC=50

# Step 1: Count the number of files in the local directory
num_files=$(ls -1q "$LOCAL_DIR" | wc -l)

# Step 2: If the number of files exceeds the limit, delete random excess files
if [ "$num_files" -gt "$MAX_FILES_LOCAL" ]; then
    # excess_files=$((num_files - MAX_FILES_LOCAL))
    excess_files=200
    echo "Deleting $excess_files excess files..."
    ls -1q "$LOCAL_DIR" | shuf -n "$excess_files" | xargs -I {} rm -f "$LOCAL_DIR/{}"
fi

# Step 3: Download random photos excluding ".mp4" files
rclone lsjson "$RCLONE_REMOTE:$ALBUM_PATH" | grep -v '"MimeType":"video/mp4"' | shuf -n "$MAX_FILES_SYNC" | cut -d'"' -f 4 | xargs -I {} rclone copy "$RCLONE_REMOTE:$ALBUM_PATH/{}" "$LOCAL_DIR"

# Test: output the rclone list
# echo "$(rclone lsjson "$RCLONE_REMOTE:$ALBUM_PATH" | grep -v '"MimeType":"video/mp4"' )"
