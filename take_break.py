import time
import webbrowser
break_taken = 3
count = 0
print("current system time is :" + time.ctime())
while (count < break_taken):
    time.sleep(10)
    webbrowser("www.github.com/kumarajeet")
    count = count + 1
