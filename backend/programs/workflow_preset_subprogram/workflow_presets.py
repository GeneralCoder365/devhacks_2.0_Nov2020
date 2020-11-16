try:
    # imports all necessary packages & modules
    import os
    import webbrowser

# except case to handle import failure
except Exception as e:
    print("Some of the required libraries are missing! {}".format(e))


# Note: ALL DATA FOR THIS SUBPROGRAM IS STORED IN preset_data.dat



# formats a new preset's data to ready it for addition to the .dat file
# child of master_preset_adder()
def format_preset(new_preset):
    new_preset_entry = ""
    i = 0
    while i < len(new_preset):
        if (i == 0):
            new_preset_entry = str(new_preset[0]) + " | "
        elif(i < len(new_preset) - 1):
            new_preset_entry = new_preset_entry + str(new_preset[i]) + " | "
        else:
            new_preset_entry = new_preset_entry + str(new_preset[i]) + "\n"
        
        i = i + 1
    
    return new_preset_entry

# appends the new preset line entry to preset_data.dat
# child of master_preset_adder()
def add_preset(formatted_preset):
    # sets to appending mode
    preset_data_file = open("backend/programs/workflow_preset_subprogram/preset_data.dat", "a")
    # appends new preset to preset_data.dat
    preset_data_file.write(formatted_preset)
    preset_data_file.close()

# lets the user create a new preset and add it to preset_data.dat
# child of master_preset_action_manager(action)
def master_preset_adder(preset_array):
    # gets all of the presets data from preset_data.dat and organizes it
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    
    i = 0
    preset_name_exists = False
    while i < len(preset_lines_array):
        preset_line_array = preset_lines_array[i].split(" | ")
        if(preset_array[0] == preset_line_array[0]):
            preset_name_exists = True
            i = len(preset_lines_array)
        else:
            preset_name_exists = False
            i = i + 1
    
    if(preset_name_exists == False):
        new_preset = format_preset(preset_array)
        add_preset(new_preset)
    else:
        print("This preset already exists!")

    # adds formatted data for new preset to preset_data.dat
    # add_preset(format_preset(new_preset))

    # gathers preset name
    # new_preset_name = input("Please enter the name of the new preset(no spaces!): ")
    # preset_urls = []

    # gathers as many urls/absolute file paths the user wants for the preset
    # more_urls = True
    # while more_urls == True:
        # url_or_application_or_file = input("Would you like to add a url or a file/application path? Please type 0 for a url and 1 for an application/file: ")
        # url_application_file = input("Please enter the url or the ABSOLUTE file path(PLEASE USE / INSTEAD OF \) of the application/file you would like to add to the preset" 
        # + "\n [please make sure that you have copied the full url!]"
        # + "\n [please make sure your file path is formatted correctly!]: ")

        # preset_urls.append(url_application_file)

        # continue_adding_to_preset = input("Would you like to continue adding to this preset? 0 for yes and 1 for no: ")

        # if(continue_adding_to_preset == "0"):
            # more_urls = True
        # elif(continue_adding_to_preset == "1"):
            # more_urls = False
        # else:
            # print("Please enter a valid input!")
            # more_urls = True
    
    # adds the preset name to the front of the array containing the urls/absolute file paths the user wants for the preset
    # preset_urls.insert(0, new_preset_name)

    # design/organization only!
    # new_preset = preset_urls

    # adds formatted data for new preset to preset_data.dat
    # add_preset(format_preset(new_preset))



# determines whether a given item to open is a url or an application/file's file_path
# child of master_preset_caller(action)
def url_or_filepath(individual_to_open):
    try:
        # Checks for an alphabet as the first character and then a : as the second character in the string
        # This alerts as to whether the given item is a url or an application/file's file_path
        if (((individual_to_open[0].lower()).isalpha() == True) and (individual_to_open[1] == ":")):
            individual_to_open_1 = r'%s' %individual_to_open
            # starts file/application if given item is a file path
            os.startfile((str(individual_to_open_1)))
        else:
            # opens url in the default browser
            webbrowser.open(individual_to_open)
    
    # except case to account for failure to open a url/file/application and alerts which one failed
    except:
        print("Could not open " + str(individual_to_open))

# opens all necessary urls/files/applications
# child of master_preset_caller(action)
def line_reader_and_opener(preset_line_array):
    # removes preset name from to open array
    to_open = preset_line_array
    to_open.pop(0)
    
    # opens all urls/files/applications in the to open array one by one
    i = 0
    while i < len(to_open):
        url_or_filepath(preset_line_array[i])
        i = i + 1

# finds the requested preset from preset_data.dat and opens all urls/files/applications for the preset
# child of master_preset_action_manager(action)
def master_preset_caller(action):
    # gets all of the presets data from preset_data.dat and organizes it
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    preset_name = action
    preset_name = preset_name.replace("1 ", "")

    preset_line = 0
    desired_line = 0

    # finds the index of the line where requested preset exists
    while preset_line < len(preset_lines_array):
        if (preset_lines_array[preset_line].find(preset_name) != -1):
            desired_line = preset_line
            preset_line = len(preset_lines_array)
        else:
            preset_line = preset_line + 1
    
    try:
        # checks for case where requested preset does not exist
        if ((preset_line == len(preset_lines_array)) and (preset_lines_array[desired_line].find(preset_name) == -1)):
            print("ERROR: This preset does not exist!")
        
        # if preset does exist, then it gets that preset line from the file contents of preset_data.dat and parses it into an array
        # it then opens all necessary urls/files/applications for the requested preset
        else:
            preset_line_array = preset_lines_array[desired_line]

            preset_line_array = preset_line_array.split(" | ")

            # opens all necessary urls/files/applications for the requested preset
            line_reader_and_opener(preset_line_array)
    
    # except case to handle blank preset_data.dat file
    except IndexError:
        print("ERROR: This preset does not exist!")



# allows user to change the data in the requested preset
# child of master_preset_editor(action)
def line_to_replace(action):
    # lets the user rewrite what urls/files/applications they want the preset to contain
    # preset_new_line = input("Please enter in what you would like this line to now read \n"
    # + "Format for n urls/file paths: url/file_path_1 | url/file_path_2 | url/file_path_3 | ... | url/file_path_n \n"
    # + "New preset data: ")

    # stores the entirety of the file data from preset_data.dat first all together and then as each line being a separate element in an array
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_data_lines = preset_data_file.readlines()
        preset_data_file.close()
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    
    # parses for the name of the preset
    preset_name = action
    preset_name = preset_name.replace("2 ", "")

    preset_line = 0
    desired_line = 0
    # finds what line the requested preset is on
    while preset_line < len(preset_lines_array):
        if (preset_lines_array[preset_line].find(preset_name) != -1):
            desired_line = preset_line
            preset_line = len(preset_lines_array)
        else:
            preset_line = preset_line + 1

    # checks for case where requested preset does not exist
    if ((preset_line == len(preset_lines_array)) and (preset_lines_array[desired_line].find(preset_name) == -1)):
        print("ERROR: This preset does not exist!")
    
    # if preset does exist, then it gets that preset line from the file contents of preset_data.dat and parses it into an array
    # it then gets the information of that line from preset_data.dat and lets the user provide the replacement line
    # it then replaces the requested preset line with the new one the user has provided
    else:
        preset_to_edit_line = str(preset_lines_array[desired_line])
        # shows user the current contents of the requested preset
        return ("Current preset data: " + preset_to_edit_line)

# allows user to edit an existing preset
# child of master_preset_action_manager(action)
def master_preset_editor(action, preset_new_line):
    # stores the entirety of the file data from preset_data.dat first all together and then as each line being a separate element in an array
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_data_lines = preset_data_file.readlines()
        preset_data_file.close()
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    
    # parses for the name of the preset
    preset_name = action
    preset_name = preset_name.replace("2 ", "")

    preset_line = 0
    desired_line = 0
    # finds what line the requested preset is on
    while preset_line < len(preset_lines_array):
        if (preset_lines_array[preset_line].find(preset_name) != -1):
            desired_line = preset_line
            preset_line = len(preset_lines_array)
        else:
            preset_line = preset_line + 1

    try:
        # checks for case where requested preset does not exist
        if ((preset_line == len(preset_lines_array)) and (preset_lines_array[desired_line].find(preset_name) == -1)):
            print("ERROR: This preset does not exist!")
        
        # if preset does exist, then it gets that preset line from the file contents of preset_data.dat and parses it into an array
        # it then gets the information of that line from preset_data.dat and lets the user provide the replacement line
        # it then replaces the requested preset line with the new one the user has provided
        else:
            preset_to_edit_line = str(preset_lines_array[desired_line])
            # shows user the current contents of the requested preset
            # print("Current preset data: " + preset_to_edit_line)

            new_line = ""

            # checks to make sure the user is not trying to force a blank preset
            if ((preset_new_line != "") and (preset_new_line != " ")):
                # creates and returns the new string that will be the line replacing the current line for the requested preset
                new_line =  preset_new_line
            else:
                print("This is not a valid new line entry!")

            preset_data_lines[desired_line] = new_line + "\n"

            # replaces the requested preset line with the new one the user has provided
            with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'w+') as preset_data_file:
                preset_data_file.writelines(preset_data_lines)

                preset_data_file.close()
    
    # except case to handle blank preset_data.dat file
    except IndexError:
        print("ERROR: This preset does not exist!")    



# allows user to delete the requested preset
# largely same as master_preset_editor(action)
# child of master_preset_action_manager(action)
def master_preset_deleter(action):
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_data_lines = preset_data_file.readlines()
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    
    preset_name = action
    preset_name = preset_name.replace("3 ", "")

    preset_line = 0
    desired_line = 0
    while preset_line < len(preset_lines_array):
        if (preset_lines_array[preset_line].find(preset_name) != -1):
            desired_line = preset_line
            preset_line = len(preset_lines_array)
        else:
            preset_line = preset_line + 1


    try:
        if ((preset_line == len(preset_lines_array)) and (preset_lines_array[desired_line].find(preset_name) == -1)):
            print("ERROR: This preset does not exist!")
        else:
            # deletes the requested preset line from the stored data from preset_data.dat
            del preset_data_lines[desired_line]

            # rewrites preset_data.dat with the modified data line by line
            with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'w+') as preset_data_file:
                for line in preset_data_lines:
                    preset_data_file.write(line)

                preset_data_file.close()
    except IndexError:
        print("ERROR: This preset does not exist!")


# displays all existing presets
# child of master_preset_action_manager(action)
def master_preset_display_all():
    # reads all data from preset_data.dat and stores it
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_data_lines = preset_data_file.readlines()
        preset_data_file.close()
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()

    # prints each line of preset_data.dat to terminal
    for i in range(len(preset_lines_array)):
        print(preset_lines_array[i])



# deletes all existing presets
# child of master_preset_action_manager(action)
def master_preset_delete_all():
    # tries to truncate the file size of preset_data.dat to 0 --> clears all preset data
    try:
        with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r+') as preset_data_file:
            preset_data_file.truncate(0)
            preset_data_file.close()
        print("Cleared!")
    
    # except case to alert that attempting to delete all preset data has failed
    except:
        print("There was a problem with clearing all presets!")



# master function to direct to subfunctions based on initial user action
# def master_preset_action_manager(action):
    # new preset
    # if (action == str("0")):
        # master_preset_adder(["skewls", "https://app.slack.com/client/T019XRPSH8T/D01EJH62342", "D:\Screenshot (914).png"])
    
    # load requested preset
    # elif (action.find("1") != -1):
        # master_preset_caller(action)
    
    # edit requested preset
    # elif (action.find("2") != -1):
        # print(line_to_replace(action))
        # master_preset_editor(action, "jobs | https://www.nasa.gov/centers/goddard/education/internships.html  | D:\Screenshot (914).png")
    
    # delete requested preset
    # elif (action.find("3") != -1):
        # master_preset_deleter(action)
    
    # show all presets
    # elif (action.find("4") != -1):
        # master_preset_display_all()
    
    # delete all presets
    # elif (action.find("5") != -1):
        # master_preset_delete_all()
    
    # invalid action catch all
    # else:
        # print("Please enter a valid action!")


# Call rules:
# action 0 means new preset:
    # Ex: master_preset_adder(["skewls", "https://app.slack.com/client/T019XRPSH8T/D01EJH62342", "D:\Screenshot (914).png"]
# action 1 preset_name means load said preset
    # Ex: master_preset_caller(action)
# action 2 preset_name means edit said preset:
    # Ex: print(line_to_replace(action))
    # master_preset_editor(action, "jobs | https://www.nasa.gov/centers/goddard/education/internships.html  | D:\Screenshot (914).png")
# action 3 preset_name means delete said preset
    # Ex: master_preset_deleter(action)


# Optional:
# action 4 means show all presets
# action 5 means delete all presets
# action [anything else]: