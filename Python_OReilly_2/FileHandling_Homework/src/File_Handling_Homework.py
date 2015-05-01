import os
import glob

def summarize_file_count(input_path):
    """Examines files in a directory and prints a summary """
    
    freq = {}
    
    for file in glob.glob("*"):
        if '.' in file:   
            file_type = os.path.splitext(file)[1]
            freq[file_type] = freq.get(file_type, 0) + 1
        else:
            continue
    
    sorted_list = [i for i in freq.items()]
    
    return sorted(sorted_list)

#print(summarize_file_count(os.getcwd()))

