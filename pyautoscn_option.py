#imported modules:
#pyautogui is used to take the screenshots.
#time is used to create a half second delay between screenshots.
#datetime is used to capture the date and time at which the screenshot was taken.
import pyautogui
import time
from datetime import datetime

sleepInt = int(input("How many seconds between screenshots? (eg '5' or '10': "))
#This is a function that writes the date and time for each screenshot to a text file.
def log_print():
    outfile = open('Capture_Log.txt', 'w')
    for ss, dt in sorted(screenshotLog.items()):
        outfile.write('Screenshot:' + str(ss) + '\t' + str(dt) + '\n')

#Empty dictionary for the screenshot log data
screenshotLog = {}

#30 minute loop that takes screenshot every half second.
i = 0
while i < 3600:
    i = i + 1
    now = str(datetime.now())
    pyautogui.screenshot(str(i) + "_scrnsht" + ".png")
    print("\a")
    screenshotLog[str(i)] = now
    log_print()
    time.sleep(sleepInt)
    
