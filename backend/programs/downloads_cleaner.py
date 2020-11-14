import os
import time
import datetime

home = os.path.expanduser('~')

xdays = float(input("Enter x number of days so that the program deletes all files older than x days: "))

today = datetime.datetime.today()

path = home + '/Downloads/'
filesearch = os.listdir(path)

for f in filesearch:
    print(f)

print("These are all your files in the downloads folder")

for p in filesearch:
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(home+'/Downloads/'+p))
    duration = today - mtime
    if duration.days > xdays and p.endswith(".dmg" or ".exe") != True:
        os.remove(home+'/Downloads/'+p)
        print(p+" has been removed")
        print(mtime)
        print(duration)