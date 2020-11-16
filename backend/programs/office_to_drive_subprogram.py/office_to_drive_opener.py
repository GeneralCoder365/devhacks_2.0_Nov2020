try:
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import os
    import webbrowser
except Exception as e:
    print("Some of the required libraries are missing! {}".format(e))

#Enter what file name you want to put in and the path to the file
def master_office_to_drive_conversion(file, path):
    file_name = file
    
    auth = GoogleAuth()

    auth.LocalWebserverAuth()

    drive = GoogleDrive(auth)

    path_search = path
     
    file_iteration(file, path_search, drive)

#looks for the specific file and then if the file is found in the path then it gets uploaded to Google Drive
def file_iteration(drive_file_name, folder, google_drive):
    try:
        if (os.path.exists(folder)) and (folder.endswith(".docx" or ".pptx" or "xlsx") == True):
                f = google_drive.CreateFile({'title': drive_file_name}) 
                f.SetContentFile(os.path.join(drive_file_name, folder)) 
                f.Upload()  
                f = None
                webbrowser.open('https://drive.google.com/drive/recent')
    except:
        print("Trouble accessing the file")

#For example I want my document to be named "3.1_Worksheet.docx" and I also put in a path to the file that I want uploaded to Google Drive
master_office_to_drive_conversion("Week 5_ Beginner Slides - 10_30_2020.pptx", "D:/Week 5_ Beginner Slides - 10_30_2020.pptx")
