import os
import shutil
import time
from notifypy import Notify

notification = Notify()

FConfig = open("config.txt", 'r')
DConfig = FConfig.readlines()
FConfig.close()

from_addr = DConfig[0].replace("\n", "")
dest_addr = DConfig[1].replace("\n", "")
skip_files = DConfig[2:]

#Removing '\n' from the filenames in the variable 'skip_files'
y = []
for i in skip_files:
    x = i.replace("\n", "")
    y.append(x)
skip_files = y
del x,y


def monitor_folder(src_folder, dst_folder, skip_list):
    # Create destination folder if it does not exist
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)


    # Start monitoring the source folder for new files
    while True:

        # Get list of files in the source folder
        src_files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]
        y = []
        for i in src_files:
            if i[0] == "~":
                continue
            else:
                y.append(i)
        src_files = y
        del y

        # Check for new files in the source folder
        new_files = list(set(src_files) - set(skip_list))
        c = 0

        # Move new files to the destination folder
        for file in new_files:
            src_path = os.path.join(src_folder, file)
            dst_path = os.path.join(dst_folder, file)

            if os.path.exists(dst_path):
                pass
            else:
                c+=1
                shutil.move(src_path, dst_path)

            if c>0:
                x = str(c) + " file(s) moved"
                notification.title = "Desktop Cleared"
                notification.message = x
                notification.send()
                del x

        time.sleep(60)

monitor_folder(from_addr, dest_addr, skip_files)
