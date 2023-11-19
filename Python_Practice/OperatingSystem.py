import os
import sys
import time
#Write a Python program to get the name of the operating system (Platform independent), 
# information of the current operating system, current working directory, print files 
# and directories in the current directory, and raise errors if the path or file name is invalid.
def print_OS_info():
    print("Current Operating System: ", os.name)
    print("Current working dir: ", os.getcwd())
    print("List of files and dirs in the cwd: ", os.listdir("."))
#print_OS_info()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to scan a specified directory and identify the subdirectories and files.
def scan_dir(root):
    for entry in os.scandir(root):
        if entry.is_dir():
            typ = 'dir'
        elif entry.is_file():
            typ = 'file'
        elif entry.is_symlink():
            typ = 'link'
        else:
            typ = 'unknown'
        print('{name:25} {typ}'.format(name=entry.name,typ=typ,))
#scan_dir("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\PythonPractice")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to check access to a specified path. Test the existence, readability, writability and executability of the specified path.
#print('Exist:', os.access("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\PythonPractice", os.F_OK))
#print('Readable:', os.access("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\PythonPractice", os.R_OK))
#print('Writable:', os.access("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\PythonPractice", os.W_OK))
#print('Executable:', os.access("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\PythonPractice", os.X_OK))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date and time of a specified path.
def info_path(path):
    stat_info = os.stat(path)
    print('Path Name ({}):'.format(path))
    print('Size:', stat_info.st_size)
    print('Permissions:', oct(stat_info.st_mode))
    print('Owner:', stat_info.st_uid)
    print('Device:', stat_info.st_dev)
    print('Created     :', time.ctime(stat_info.st_ctime))
    print('Last modified:', time.ctime(stat_info.st_mtime))
    print('Last accessed:', time.ctime(stat_info.st_atime))
info_path("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\PythonPractice\\OperatingSystem.py")