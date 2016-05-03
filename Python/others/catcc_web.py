import webbrowser as web
import time
import os
i=0
while True:
    while i<=5:
        web.open_new_tab('https://www.baidu.com')
        i=i+1
        time.sleep(0.8)
    else:
        os.system('taskkill /F /IM chrome.exe')   
