import os
import time
import datetime

home = os.path.expanduser('~')

x_days = input("Enter x number of days so that the program deletes all files older than x days: ")

today = datetime.datetime.today()

path = home + '/Downloads/'
filesearch = os.listdir(path)

for p in filesearch:
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(home+'/Downloads/'+p))
    duration = today - mtime
    if duration.days < x_days:
        os.remove(home+'/Downloads/'+p)
        print(p+" has been removed")
        print(mtime)
        print(duration)