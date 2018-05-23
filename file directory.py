#my two tier file directory markdown hyperlink generator 


import os
path = #insert directory name here
core_path = (os.listdir(path))

#first lists that the names folder
for files in core_path:
    print ("\n", files,"\n")
    file_list = (os.listdir(r'{}\{}'.format(path,files)))
    # Second tier creates dictionay of the name of the files and path to the file
    dirc={}
    for name in file_list:
        dirc[name]=r'{}\{}\{}'.format(path, files, name)

    #Genrate markdown syntax for file name and path
    for key, value in dirc.items() :
        print("[{}]({})\n".format(os.path.splitext(key)[0], value))
