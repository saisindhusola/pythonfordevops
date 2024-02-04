import os
folders = input("Provide a list of folders names with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name. given folder doesn't exist: "+ folder)
        break #To ignore the wrong folder and proceed with the next folders use continue instead of break.
    except PermissionError:
        break
        print("No access to this folder: " + folder) #If folder has any passwords.
    
    print("===listing files for the folder - " + folder)
    #print(files) #if directly printing files, it print's in list format.
    #To print in order, we write for loop 

    for file in files:
        print(file)
    #if given /Apps /Users as input it prints the list of files in the folder/
    
    #If same program written using function method, It is easy to uderstand.