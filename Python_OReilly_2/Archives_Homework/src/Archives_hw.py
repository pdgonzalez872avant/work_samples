"""Zips files in a directory"""

import os
import tempfile
import zipfile
import glob

def create_archive_directory_only(input_path):
    archive_fn = os.path.join(input_path, "my_arquive.zip")
    zf = zipfile.ZipFile(archive_fn, "w")
    
    file_names = glob.glob("*") # Pat

    for fn in file_names:
       
        base = os.path.basename(fn) # Pat
        
        if os.path.isfile(fn):
            #print(os.path.basename(input_path)+os.sep+base)
            separators = "//"
            zf.write(fn, arcname=os.path.basename(input_path)+separators+base)
            
    zipped_list = zf.namelist()
    zf.close()
    
    final_list = []
    for i in zipped_list:
        sep1 = r"/"
        sep2 = os.sep
        #final_list.append(str(i).replace(sep1, sep2)) 
        if '.zip' in i:
            pass
        else:
            final_list.append(str(i).replace(sep1, sep2))
    
    return sorted(final_list)
