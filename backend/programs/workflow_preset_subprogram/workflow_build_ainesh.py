try:
    import os
    import sys
    import webbrowser
except Exception as e:
    print("Some of the required libraries are missing! {}".format(e))

# action 0 means new preset
# action 1 preset_name means load said preset
# action 2 preset_name means edit said preset
# action 3 preset_name means delete said preset
action = input("Enter 0 to create a new preset \n or \n Enter the name of an existing preset to load it: ")



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

def add_preset(formatted_preset):
    # sets to appending mode
    preset_data_file = open("backend/programs/workflow_preset_subprogram/preset_data.dat", "a")
    preset_data_file.write(formatted_preset)
    preset_data_file.close()

def master_preset_adder():
    new_preset_name = input("Please enter the name of the new preset(no spaces!): ")
    preset_urls = []

    more_urls = True
    while more_urls == True:
        # url_or_application_or_file = input("Would you like to add a url or a file/application path? Please type 0 for a url and 1 for an application/file: ")
        url_application_file = input("Please enter the url or the ABSOLUTE file path(PLEASE USE / INSTEAD OF \) of the application/file you would like to add to the preset" 
        + "\n [please make sure that you have copied the full url!]"
        + "\n [please make sure your file path is formatted correctly!]: ")

        preset_urls.append(url_application_file)

        continue_adding_to_preset = input("Would you like to continue adding to this preset? 0 for yes and 1 for no: ")

        if(continue_adding_to_preset == "0"):
            more_urls = True
        elif(continue_adding_to_preset == "1"):
            more_urls = False
        else:
            print("Please enter a valid input!")
            more_urls = True
    
    preset_urls.insert(0, new_preset_name)

    new_preset = preset_urls

    add_preset(format_preset(new_preset))



def url_or_filepath(individual_to_open):
    try:
        if (((individual_to_open[0].lower()).isalpha() == True) and (individual_to_open[1] == ":")):
            individual_to_open_1 = r'%s' %individual_to_open
            os.startfile((str(individual_to_open_1)))
            print("Hello")
        else:
            webbrowser.open(individual_to_open)
    except:
        print("Could not open " + str(individual_to_open))
        e = sys.exc_info()
        print(e)

def line_reader_and_opener(preset_line_array):
    to_open = preset_line_array
    to_open.pop(0)
    
    i = 0
    while i < len(to_open):
        url_or_filepath(preset_line_array[i])
        i = i + 1

def master_preset_caller(action):
    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'r') as preset_data_file:
        preset_lines_array = [line.rstrip() for line in preset_data_file]
        preset_data_file.close()
    preset_name = action
    preset_name = preset_name.replace("1 ", "")

    preset_line = 0
    desired_line = 0
    while preset_line < len(preset_lines_array):
        if (preset_lines_array[preset_line].find(preset_name) != -1):
            desired_line = preset_line
            preset_line = len(preset_lines_array)
        else:
            preset_line = preset_line + 1
    
    preset_line_array = preset_lines_array[desired_line]

    preset_line_array = preset_line_array.split(" | ")

    line_reader_and_opener(preset_line_array)



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

    del preset_data_lines[desired_line]

    with open("backend/programs/workflow_preset_subprogram/preset_data.dat", 'w+') as preset_data_file:
        for line in preset_data_lines:
            preset_data_file.write(line)

        preset_data_file.close()
    
    

def master_preset_action_manager(action):
    if (action == str("0")):
        master_preset_adder()
    elif (action.find("1") != -1):
        master_preset_caller(action)
    elif (action.find("2") != -1):
        print()
    elif (action.find("3") != -1):
        master_preset_deleter(action)
    else:
        return "Please enter a valid action!"

master_preset_action_manager(action)