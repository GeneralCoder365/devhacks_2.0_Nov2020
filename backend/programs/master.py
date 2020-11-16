import sys

tool_select = input("Tool Select\n"
+ "Enter 0 to launch the preset controller tool\n"
+ "Enter 1 to launch the downloads cleaner tool\n"
+ "Tool: ")

if(tool_select == "0"):
    sys.path.append("backend/programs/workflow_preset_subprogram")
    import workflow_presets as wp
    wp.master()
elif(tool_select == "1"):
    sys.path.append("backend\programs\downloads_cleaner_subprogram")
    import downloads_cleaner as dc
    dc.master()
else:
    print("Please select a valid tool!")