import subprocess
import time
import os

def execute_shell_command(command):
    try:
        # Run the shell command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Print any error messages
        if result.stderr:
            print("Error Output:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        # Handle the case where the command returns a non-zero exit code
        print(f"Error: Command '{e.cmd}' failed with exit code {e.returncode}")
        print("Error Output:")
        print(e.stderr)

def read_file_into_variable(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file into a variable
            file_content = file.read()
            return file_content

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def toggle_window():
    # print('toggle window start')
    curId = read_file_into_variable('/home/pi/window_id_current.txt').strip()
    mmId = read_file_into_variable('/home/pi/window_id_magicmirror.txt').strip()
    pfId = read_file_into_variable('/home/pi/window_id_picframe.txt').strip()
    # print('cur: ' + curId)
    # print('mm: ' + mmId)
    # print('pf: ' + pfId)
    
    if (curId == mmId):
        # switch to picframe
        # print('toggle to picframe')
        execute_shell_command('DISPLAY=:0 xdotool windowraise ' + pfId)
        os.system('cat /home/pi/window_id_picframe.txt > /home/pi/window_id_current.txt')
    elif (curId == pfId):
        # switch to magicmirror
        # print('toggle to magicmirror')
        execute_shell_command('DISPLAY=:0 xdotool windowraise ' + mmId)
        os.system('cat /home/pi/window_id_magicmirror.txt > /home/pi/window_id_current.txt')

    # print('toggle window end')

def init():
    # Collect the window ids ecen if the files already exist
    execute_shell_command('DISPLAY=:0 xwininfo -tree -root | awk \'/MagicMirror/{gsub(/^[ \t]+/, ""); print substr($0, 1, 8)}\' > /home/pi/window_id_magicmirror.txt')
    execute_shell_command('DISPLAY=:0 xwininfo -tree -root | awk \'/3840x2160/{gsub(/^[ \t]+/, ""); print substr($0, 1, 8)}\' > /home/pi/window_id_picframe.txt')

    time.sleep(2)

    # Save the magic-mirror id into the "current window id" file since it'll usually be the last process to start up
    execute_shell_command('cat /home/pi/window_id_magicmirror.txt > /home/pi/window_id_current.txt')