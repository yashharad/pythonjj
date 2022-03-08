import os
import shutil

source = input(" ^ Enter_SOurce_Folder_Name ^ ")
destination = input  ("* Enter_Destination_Folder_Name *")

source=source+"/"
destination=destination+"/"

list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),destination)