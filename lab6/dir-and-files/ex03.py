import os 

path = r'/Users/admin/pp2/lab6'
# path.replace('\\', '/')

if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')