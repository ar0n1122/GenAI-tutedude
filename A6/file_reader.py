# Task 4
filename= input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        content = file.readlines()
        for i in range(3):  
            print(content[i])
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except PermissionError:
    print("You do not have permission to read this file.")

finally:
    print("File operation completed.")