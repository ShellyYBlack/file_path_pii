# Finding PII in file paths
Identify file paths that may contain PII based on a list of regular expressions. The script will search for the regex in file names or directory names. However, if a directory is empty, it will not be included.
## Instructions
1. Edit rlist.txt to contain strings or regular expressions you want to search for.
1. Run the script `python3 file_path_pii.py`
1. Open file_path_pii.csv to view the results. The first column shows the file paths and the second column shows the match.