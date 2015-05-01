"""Function takes 2 arguments, and keeps the high score of each input"""

import os
import tempfile
import zipfile
import glob


def create_archive_directory_only(path):
    archive_fn = os.path.join(path, r"\my_arquive.zip")
    zf = zipfile.ZipFile(archive_fn, "w")
    zf.close()
    file_list = []
    #for file in path:
    for file in glob.glob(os.path.join(path, "*")):

        file_list.append(os.path.split(file))
        #if os.path.isfile(file): #then add to 
            #file_list.append(os.path.split(file))
            #file_list.append(file)
    #for isfile in file_list:
        
    return sorted(file_list)
    #return archive_fn
    #return zf
    #return glob.glob(os.path.join(archive_fn, "*"))
    #return os.path(archive_fn)
    #return file_list

path = "v:\workspace"
origdir = os.getcwd()
toprint = glob.glob(os.path.join(origdir, "*"))

#print(create_archive_directory_only(toprint))


