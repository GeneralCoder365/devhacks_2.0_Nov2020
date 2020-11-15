import os
import time
import datetime
import sys
import sched
import schedule

#/Users/username
home = os.path.expanduser('~')

#instructions
print("\nThis is the downloads cleanup section of the program, if you want to change preferences, please type 'preferences' and if you want to exit the program, please type 'exit' \n")
print("The program prints out every file you have in the Downloads folder of your computer and if a file is older than x number of days, the program will also notify you about what files have been removed \n")
print("\nDecimal values can be used for this to manipulate the values into smaller values like hours and minutes even\n")
print("\nBE CAREFUL OF THE VALUES YOU PUT IN FOR THE CLEANUP BECAUSE YOU DON'T WANT NEARLY EVERY FILE TO BE DELETED\n")

#pause for 3 seconds
time.sleep(3)


#stops the program
def stop_program():
    exit()

#passes data to the dat file for how the limit of how long (in days) a file can stay in the downloads folder
def add_data_for_days(formatted_data):
    cleanupdays_data_file = open("backend/programs/downloads_cleaner_subprogram/data.dat", "w+")
    cleanupdays_data_file.write(formatted_data)
    cleanupdays_data_file.close()

def read_data_for_days():
    with open("backend/programs/downloads_cleaner_subprogram/data.dat", "r") as days_data:
        user_days = days_data.readlines()
        return user_days
        user_days.close()

#variables that wont change unless you type 'preferences'

xdays = float(input("Enter x number of days so that the program deletes all files older than x days: "))
(add_data_for_days(str(xdays)))
user_days = read_data_for_days()
user_days = user_days[0]
user_days = float(user_days)
print("user_days: " + str(user_days))



#does the task of accessing files and deleting them alongisde closing the program or setting preferences
def instant_task():
    today = datetime.datetime.today()

    #path to Downloads
    path = home + '/Downloads/'
    #this will be used to iterate over every file in Downloads
    filesearch = os.listdir(path)

    
    #iterates through all the Downloads files
    for p in filesearch:
        #time the file was added to computer
        timeadded = datetime.datetime.fromtimestamp(os.path.getmtime(home+'/Downloads/'+p))
        #difference between the day today and the time the file was added
        duration = today - timeadded
        #deleted files will be stored in this array
        deleted_files_array = []
        try:
            #dmg, exe, app files arent going to be deleted
            if (duration.days > user_days) and (p.find(".dmg" or ".exe" or ".app") == -1):
                os.remove(home+'/Downloads/'+p)
                deleted_files_array.append(p)
                print(p+" has been removed")
                print(timeadded)
                print(duration)
        #if a file fails to delete because it doesn't have a file format (common in OS) then this exception appears
        except:
            print(p+" has failed to delete")


    exit_input = str(input())
    
    #lets you exit program
    if exit_input == "exit":
        stop_program()


#does the task
instant_task()


