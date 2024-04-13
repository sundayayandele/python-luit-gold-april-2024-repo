import os

#This function creates a list of dictionaries from the filepaths obtained by the walk_files() function
def print_filepaths(src_filepath = "."):
    #Recursively obtain the list of files from walk_files function
    filepath_list = walk_files(src_filepath)
    file_info_list = []
    
    #iterate through each filepath in filepath_list and create
    #dictionary items to add to file_info_list
    for filepath in filepath_list:
        #Fetch the size of the file for the filepath that is inputted
        #Uses os.getcwd() function to use as the filepath if the filepath variable is equal to '.'.
        #Otherwise uses the filepath variable instead.
        if filepath == '.':
            size = os.path.getsize(os.getcwd())
        else:
            size = os.path.getsize(filepath)
        
        #Create a dictionary containing the filepath and the size as key/pair values    
        file_info = {"path": filepath, "size": size}
        #Add the dictionary item to the file_info_list list
        file_info_list.append(file_info)
    
    #iterate through each item in file_info_list and print each item
    for file in file_info_list:
        print(file)

#This function goes through all of the files and subdirectories in the file path specified by the user
#and appends all filepaths to a list. The function then returns this list
def walk_files(src_filepath = "."):
    filepath_list = []
   
    #This for loop uses the os.walk() function to walk through the files and directories
    #and records the filepaths of the files to a list
    for root, dirs, files in os.walk(src_filepath):
        
        #iterate through the files currently obtained by os.walk() and
        #create the filepath string for that file and add it to the filepath_list list
        for file in files:
            #Checks to see if the root is '.' and changes it to the correct current
            #working directory by calling os.getcwd(). Otherwise root_path will just be the root variable value.
            if root == '.':
                root_path = os.getcwd() + "/"
            else:
                root_path = root
            
            #This if statement checks to see if an extra '/' character is needed to append 
            #to the filepath or not
            if (root_path != src_filepath) and (root != '.'):
                filepath = root_path + "/" + file
            else:
                filepath = root_path + file
            
            #Appends filepath to filepath_list if filepath does not currently exist in filepath_list
            if filepath not in filepath_list:
                filepath_list.append(filepath)
                
    #Return filepath_list        
    return filepath_list

#Call print_filepaths function with the specified filepath
print_filepaths('/home/ec2-user/environment/test_folder/')