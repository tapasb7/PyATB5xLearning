import json
import os

print(os.getcwd())
print(os.name)

with open('my_file.txt', 'w') as f:
    f.write('hello world')
