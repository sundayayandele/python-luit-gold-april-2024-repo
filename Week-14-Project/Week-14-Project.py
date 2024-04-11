import os
current_files = os.listdir('.')
#print(current_files)
#print(os.listdir('.'))
#print(os.getcwd())
current_filepaths = []

for file in current_files:
    #if file.isdir()
    #print(file)
    #i == false:
    #if os.path.isdir(file) == 
    if os.path.isfile(file):
        #print(os.path.isfile(file), file)
        
        filepath = os.getcwd() + '/' + file
        size = os.path.getsize(filepath)
        file_info = {"path": filepath, "size": size}
        current_filepaths.append(file_info)
        #print(filepath, size)
        #print(file_info)
    #print(filepath)
    #print(os.path.getsize(filepath))
    #filepath = 
    #current_filepaths.append()
print(current_filepaths)