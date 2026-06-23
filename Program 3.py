# write a python program to print the content of a directory using the os module. use chatgpt 
# os is  inbuilt module in python 

# Import the built-in os module, which provides functions for interacting with the operating system
import os

# Store the path of the directory whose contents we want to display
directory = "/"  # Replace this with the actual directory path

# Start a try block to handle possible errors
try:

    # os.listdir(directory) returns a list of all files and folders
    # inside the specified directory
    for item in os.listdir(directory):

        # Print the name of each file or folder
        print(item)

# This block executes if the specified directory does not exist
except FileNotFoundError:

    # Display an error message
    print("Directory not found.")

# This block executes if the program does not have permission
# to access the directory
except PermissionError:

    # Display an error message
    print("Permission denied.")