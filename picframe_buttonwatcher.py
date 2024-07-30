import os
import time
import board
import digitalio
import RPi.GPIO as GPIO 
import picframe_windowmanager as windowManager

windowManager.init()

# setup the toggle button
btn1 = digitalio.DigitalInOut(board.D24)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.D23)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

def shutdown(channel):  
   os.system("sudo shutdown -h now")  
def restart():
   os.system("sudo shutdown -r now")
def toggleScreenPower(channel):
   os.system("")
def toggleOrientation():
   os.system("DISPLAY=:0 xrandr --output HDMI-1 --rotate left")
def toggle(channel):
    windowManager.toggle_window()

# GPIO.add_event_detect(23, GPIO.FALLING, callback = toggle, bouncetime = 2000)  
# GPIO.add_event_detect(24, GPIO.FALLING, callback = restart, bouncetime = 2000) 

while True:
 
   if not btn1.value:#and btn2.value:
   # if 0 not in (btn1.value, btn2.value):
      time.sleep(0.2)  # wait 50 ms see if switch is still on
      if not btn1.value:
         # print('toggle window')
         windowManager.toggle_window()
         time.sleep(1)

   if not btn2.value:
      time.sleep(3)  # wait 50 ms see if switch is still on
      if not btn2.value:
         # print('restart')
         restart()

   # if 0 in (btn1.value, btn2.value):
   #    time.sleep(2)  # wait 50 ms see if switch is still on
   #    if 0 in (btn1.value, btn2.value):
   #       # print('orient')
   #       toggleOrientation()
