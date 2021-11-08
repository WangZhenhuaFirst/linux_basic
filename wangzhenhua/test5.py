import sys
import os

for arg in sys.argv:
    print(arg)

path = '/usr/bin/'
dirs = os.listdir(path)
for file in dirs:
    if file[0] == 'm':
        print(file)
