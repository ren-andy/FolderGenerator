import os
import sys

# Check if given path exists
def check_path(path): 
    exists = os.path.isdir(path)
    return exists

# Generates named folder based on given path
def create_directory(path, new_dir_name): 
    try:
        os.makedirs(path + "\\" + new_dir_name)
    except FileExistsError: 
        return "exists"
    except Exception as e: # Catches rest of errors 
        print(e)
        return "failed"

    return "success"


""" Description: if path is i.e "C:\\....\", CMD turns the '"\' sequence into '"' 
    Thus, argv includes the rest of the parameters as part of the path string, making argv length = 3
    Function will split the path string into desired parameters. """
def splitargv(argv_inst):
    split_index = argv_inst[2].find("\" ")

    # Split 3rd element into path and parameters
    temp_path = argv_inst[2][:split_index]
    temp_new_dirs = argv_inst[2][split_index+2:]
    argv_inst[2] = temp_path

    # Remove possible excessive spaces after "\ 
    temp_new_dirs = ' '.join(temp_new_dirs.split())

    # Split parameters into array to be combined with rest of argv  
    temp_array = temp_new_dirs.split(" ")
    argv_inst = argv_inst + temp_array
    return argv_inst

def main():
    # Usage: python directorygen.py -[flag] [path] new_dir_1 new_dir_2...

    # if empty length, print instructions
    if (len(sys.argv) == 1):
        print("\nUsage: python directory_gen.py -[flag] [\"<path>\"] <folder_name_1> <folder_name_2>...")
        print("Flags:")
        print("\t\"-p\" \"<path>\" <folder_name_1> <folder_name_2>... --> creates new directories in given path.")
        print("\t Note: For spaced new folder names, i.e \"Folder Name\", use quotations.")
        return

    # 3 execution cases
    if(sys.argv[1] == "-p"): # Specific path specified

        # See splitargv() comment
        if(len(sys.argv) == 3):
          sys.argv = splitargv(sys.argv)
        
        # Remove the flag and make argv adjustments so
        # flag "-p" folder creation is consistent with flagless folder creation
        sys.argv = sys.argv[:1] + sys.argv[2:]

        path = sys.argv[1]

        first_dir_param = 2
        # Check local path 
        if(not check_path(path)):
            print("\nError: Cannot find the path, please input a valid path")
            print("Path syntax i.e: C:\\Folder1\\Folder2\\...")
            return
    elif(sys.argv[1][0] == "-"): # Invalid flag used 
        print("\nError: Incorrect flag.")
        print("Usage: python directory_gen.py -[flag] [\"<path\"] <folder_name_1> <folder_name_2>...")
        print("Flags:")
        print("\t\"-p\" \"<path>\" <folder_name_1> <folder_name_2>... --> creates new directories in given path.")
        print("\t Note: For spaced new folder names, i.e \"Folder Name\", use quotations.")
        return 
    else: # Assume use of local path 
        path = os.getcwd()
        first_dir_param = 1 
  
    print("Creating folders...")

    # Create passed folder_names  
    for i in range(first_dir_param, len(sys.argv)):
        result = create_directory(path, sys.argv[i])
        if(result == "success"):
            print(f"\nCreated directory \"{sys.argv[i]}\" successfully in \"{path}\".")  
        elif(result == "exists"):
           print(f"\nError: Unable to create directory \"{sys.argv[i]}\" in \"{path}\".")
           print("Directory already exists.") 
        else: 
            print(f"\nError: Unable to create directory \"{sys.argv[i]}\" in \"{path}\".")
    return
    
if __name__ == '__main__':
    main()