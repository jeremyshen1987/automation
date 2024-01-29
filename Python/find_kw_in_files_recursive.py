import sys
from pathlib import Path
from datetime import datetime


args_num = len(sys.argv)

# script name count as 1 arg - py find_kw_in_files_recursive.py (argNum 0) ./logs (argNum 1) someKeyWords (argNum 2) 
if args_num != 3:
    print('provide exactly two args: pathname and keyword')
    sys.exit(1)

keyword = sys.argv[2]

path_name = sys.argv[1]
selected_path = Path(path_name)

cur_date = datetime.now()

counter = 0

# exclude result.txt since it contains the keyword of previous search
files = [f for f in selected_path.rglob('*.txt') if f.is_file() and f.name != 'result.txt']

# use append option to avoid overwrite
with open('result.txt', 'a') as wf:
    wf.write(f'Search date: {cur_date}\n search path: {path_name} *** keyword: {keyword}\n\n')

    for f in files:

        with open(f, 'r') as rf:
            # read the file line by line, won't cause memory shortage
            for line in rf:
                
                # case insensitive search
                if(keyword.casefold() in line.casefold() ):
                    counter += 1
                    wf.write(f'file name: {f} \nkw found in: \n{line}')

    if counter == 0:
        wf.write('no kw found in any lines of any file')