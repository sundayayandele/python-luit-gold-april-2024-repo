import os

def print_filepaths(src_filepath = "."):
    current_files = os.listdir(src_filepath)
    current_filepaths = []
    #print(src_filepath)
    
    for file in current_files:
 
        #if os.path.isfile(file):
            
        if src_filepath == ".":
            filepath = os.getcwd() + '/' + file
        else:
            filepath = src_filepath + file
        size = os.path.getsize(filepath)
        file_info = {"path": filepath, "size": size}
        current_filepaths.append(file_info)

    for file in current_filepaths:
        print(file)


print_filepaths('/home/ec2-user/environment/test_folder/')
