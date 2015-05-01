import glob
import os

def latest(num=1, path="."):
    
    files = glob.glob(os.path.join(path, "*"))
    dated_files = [(os.path.getmtime(fn), os.path.abspath(fn)) for fn in files]
    dated_files.sort()
    latest_files = [f for (d, f) in dated_files[-num:]] 
    latest_files.reverse()
    return latest_files


