import os
import shutil
import subprocess
import psutil
import time

# Checks whether the given value is a number for the folder names
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Finds the latest version folder of Opera GX
def get_highest_version_folder(base_path):
    # Gathers all the folders in the Opera GX folder
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    valid_folders = []

    # Only gets folders that are versions of Opera GX
    for folder in folders:
        parts = folder.split(".")
        # Checks if the folder has multiple parts in the version i.e. 102.234.45.124 and if the first part is a number
        if len(parts) > 1 and is_number(parts[0]):
            valid_folders.append(parts)

    # Checks if any folders are found
    if not valid_folders:
        print("No valid folders found.")
        return None

    # Sets the highest folder as the first folder in the list
    highest_folder = valid_folders[0]

    # Goes through valid folder to try and find the highest folder version
    for folder in valid_folders[1:]:
        for i in range(len(folder)):
            if int(folder[i]) > int(highest_folder[i]):
                highest_folder = folder
                break
            elif int(folder[i]) < int(highest_folder[i]):
                break

    # Puts the highest folder name back together when returning
    return ".".join(highest_folder)

# Copies the WidevineCdm folder to the highest version folder
def copy_to_folder(src_folder, dest_folder):
    # Get the folder name from the source path
    folder_name = os.path.basename(src_folder)
    dest_path = os.path.join(dest_folder, folder_name)
    
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    
    shutil.copytree(src_folder, dest_path)

# Closes Opera GX
def close_program(program_name):
    # Gets every process running to find Opera GX and terminate it
    for proc in psutil.process_iter(["pid", "name"]):
        if proc.info["name"] == program_name:
            try:
                proc.terminate()
                proc.wait()
            except:
                continue

# Opens Opera GX
def open_program(program_path):
    subprocess.Popen(program_path)

# Defines all the folder locations
cwd = os.path.dirname(__file__) + "\\"
base_path = os.path.expandvars(r"%localappdata%\Programs\Opera GX")
folder_to_copy = os.path.join(cwd, "WidevineCdm")
program_name = "opera.exe"  # Name of the program to close and reopen
program_path = os.path.join(base_path, "launcher.exe")  # Path to the program executable

# Get the highest version folder
highest_version_folder = get_highest_version_folder(base_path)

# Checks if there is a highest version folder
if highest_version_folder:
    # Copies WidevineCdm to the highest version folder
    dest_folder = os.path.join(base_path, highest_version_folder)
    print(f"Copying {folder_to_copy} to {dest_folder}")
    copy_to_folder(folder_to_copy, dest_folder)
    
    # Closes Opera GX
    print(f"Closing {program_name}")
    close_program(program_name)
    
    time.sleep(5)  # Wait for 5 seconds before reopening the program
    
    # Opens Opera GX
    print(f"Opening {program_name}")
    open_program(program_path)
else:
    print("No valid folder to copy to.")