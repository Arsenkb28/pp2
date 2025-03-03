import os

path = r'/Users/admin/pp2/lab6/dir-and-files/ex04.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))