import os
current_files = os.listdir('.')
print(current_files)
#print(os.listdir('.'))
#print(os.getcwd())
current_filepaths = []

for file in current_files:
    #if file.isdir()
    #print(file)
    filepath = os.getcwd() + '/' + file
    print(filepath)
    print(os.path.getsize(filepath))
    #filepath = 
    #current_filepaths.append()