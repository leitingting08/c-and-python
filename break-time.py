import time
import webbrowser

total_breaks = 3
break_count = 0

print("this program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(20*60)
    webbrowser.open("http://www.kugou.com/song/2e5h2a9.html?from_sogou")
    break_count = break_count + 1
