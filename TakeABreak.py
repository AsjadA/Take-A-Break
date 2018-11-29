import time
import webbrowser 
def take_a_break(NoOfBreaks, TimeBetweenBreaks, website):
    #TimeBetweenBreaks is in mins and must be converter to seconds
    TimeSeconds = TimeBetweenBreaks * 60
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    x = 1 
    print("This prog started on: " + time.ctime())
    while x <= NoOfBreaks:
        time.sleep(TimeSeconds)
        webbrowser.get(chrome_path).open(website, new = 2)
        x = x + 1