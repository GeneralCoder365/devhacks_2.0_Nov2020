import os
import datetime



#/Users/username
home = os.path.expanduser('~')



#instructions
# print("\nThis is the downloads cleanup section of the program, if you want to change preferences, please type 'preferences' and if you want to exit the program, please type 'exit' \n")
# print("The program prints out every file you have in the Downloads folder of your computer and if a file is older than x number of days, the program will also notify you about what files have been removed \n")
# print("\nDecimal values can be used for this to manipulate the values into smaller values like hours and minutes even\n")
# print("\nBE CAREFUL OF THE VALUES YOU PUT IN FOR THE CLEANUP BECAUSE YOU DON'T WANT NEARLY EVERY FILE TO BE DELETED\n")



# takes user input on whether they want to change timer or run cleaner
action = input("Enter 0 to run downloads cleaner \n"
+ "Enter 1 to change the deletion time check\n"
+ "Enter 2 to see the current deletion time check\n"
+ "Action: ")



#stops the program
def stop_program():
    exit()



# passes NEW data to the dat file for how the limit of how long (in days) a file can stay in the downloads folder
# child of master_downloads_cleanup_action_manager(action)
def master_cleanup_time_changer(default_x_days):
    xdays = input("Enter x number of days so that the program deletes all files older than x days\n" 
    + "Format: NON-ZERO, POSITIVE, INTEGER VALUES ONLY\n" 
    + "timer: ")
    if ((xdays != "") and (xdays != " ") and (xdays != "0") and (xdays.isnumeric() == True)):
        xdays = str(float(xdays))
    else:
        xdays = default_x_days
        print("ERROR: You did not enter a valid time -> setting timer to default value of 365 days!")
    
    try:
        cleanupdays_data_file = open("backend/programs/downloads_cleaner_subprogram/cleaner_data.dat", "w+")
        cleanupdays_data_file.truncate(0)
        cleanupdays_data_file.write(xdays)
        cleanupdays_data_file.close()
        print("Timer successfully set to " + str(xdays) + " days!")
    except:
        print("ERROR: Failed to set new time for deletion requirement!")



# reads cleaner_data.dat for timer value and returns it
# child of master_cleanup_runner()
def read_data_for_days(default_x_days):
    with open("backend/programs/downloads_cleaner_subprogram/cleaner_data.dat", "r") as days_data:
        user_days = ""
        try:
            user_days = days_data.readlines()[0]
        except IndexError:
            cleanupdays_data_file = open("backend/programs/downloads_cleaner_subprogram/cleaner_data.dat", "w+")
            cleanupdays_data_file.truncate(0)
            cleanupdays_data_file.write(default_x_days)
            cleanupdays_data_file.close()
            user_days = days_data.readlines()[0]
            
            days_data.close()
        
        return user_days



#does the task of accessing files and deleting them alongisde closing the program or setting preferences
# child of master_cleanup_runner()
def instant_task(user_days):
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

# cleans up downloads based on timer data from cleaner_data.dat
# child of master_downloads_cleanup_action_manager(action)
def master_cleanup_runner(default_x_days):
    user_days = read_data_for_days(default_x_days)
    user_days = float(user_days)
    print("cleanup minimum days: " + str(user_days))
    instant_task(user_days)



# master function to direct to subfunctions based on initial user action
def master_downloads_cleanup_action_manager(action):
    default_x_days = "365.0"
    if(action == "0"):
        master_cleanup_runner(default_x_days)
    elif(action == "1"):
        master_cleanup_time_changer(default_x_days)
    elif(action == "2"):
        print("Current Timer Value = " + str(read_data_for_days(default_x_days)))
    else:
        print("Please enter a valid action!")
        exit()



# calls master function
master_downloads_cleanup_action_manager(action)