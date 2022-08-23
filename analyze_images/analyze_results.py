from os import listdir
from os.path import isfile, join
path = '../testcases/output'
output_files = [f for f in listdir(path) if isfile(join(path, f))]
print(output_files)
s = set()
for output_file in output_files:
    f = open(join(path, output_file), 'r')
    output_str = f.read().strip('\n')
    for c in output_str:
        s.add(c)
        
# check how many characters we have
print(s)
print(len(s))
    
