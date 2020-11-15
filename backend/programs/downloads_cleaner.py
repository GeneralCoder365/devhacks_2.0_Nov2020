import os
import time
import datetime
import sys
import sched
import schedule

home = os.path.expanduser('~')

print("\nThis is the downloads cleanup section of the program, if you want to change preferences, please type 'preferences' and if you want to exit the program, please type 'exit' \n")
print("The program prints out every file you have in the Downloads folder of your computer and if a file is older than x number of days, the program will also notify you about what files have been removed \n")
print("\nDecimal values can be used for this to manipulate the values into smaller values like hours and minutes even\n")
print("\nBE CAREFUL OF THE VALUES YOU PUT IN FOR THE CLEANUP BECAUSE YOU DON'T WANT NEARLY EVERY FILE TO BE DELETED\n")

time.sleep(3)

#preferences for people to switch the values of the routine schedule and to change the limig of the number of days a file has been added to the computer but can stay in the folder
def preferences():
    xdays = float(input("Enter x number of days so that the program deletes all files older than x days: "))
    add_data_for_days(str(xdays))
    runtime = float(input("Also enter every how many days that you want a routine schedule: "))
    add_data_for_runtime(str(runtime))

#stops the program
def stop_program():
    exit()

#passes data to the dat file for how the limit of how long (in days) a file can stay in the downloads folder
def add_data_for_days(formatted_data):
    cleanupdays_data_file = open("backend/programs/workflow_preset_subprogram/data.dat", "w")
    cleanupdays_data_file.write(formatted_data)
    cleanupdays_data_file.close()

#passes data to dat file for routine scheduling periods
def add_data_for_runtime(formatted_data):
    runtime_data_file = open("backend/programs/workflow_preset_subprogram/runtime.dat", "w")
    runtime_data_file.write(formatted_data)
    runtime_data_file.close()

#variables that wont change unless you type 'preferences'
xdays = float(input("Enter x number of days so that the program deletes all files older than x days: "))
add_data_for_days(str(xdays))
runtime = float(input("Also enter every how many days that you want a routine schedule: "))
add_data_for_runtime(str(runtime))

#does the task of accessing files and deleting them alongisde closing the program or setting preferences
def instanttask():
    today = datetime.datetime.today()

    path = home + '/Downloads/'
    filesearch = os.listdir(path)

    for f in filesearch:
        print(f)

    print("These are all your files in the downloads folder")

    for p in filesearch:
        timeadded = datetime.datetime.fromtimestamp(os.path.getmtime(home+'/Downloads/'+p))
        duration = today - timeadded
        if duration.days > xdays and p.endswith(".dmg" or ".exe") != True:
            os.remove(home+'/Downloads/'+p)
            print(p+" has been removed")
            print(timeadded)
            print(duration)
    

    user_input = str(input())
    exit_input = str(input())

    if user_input == "preferences":
        preferences()
    
    if exit_input == "exit":
        stop_program()


#initially does task
instanttask()

#after a certain amount of time, it does the task again
def scheduledtask():
    instanttask()



#sets routine
schedule.every(runtime).day.do(scheduledtask)

while 1:
    schedule.run_pending()
    time.sleep(1)

