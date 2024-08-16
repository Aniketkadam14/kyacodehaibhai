#Open (or create) a file named 'example.txt' in write mode
with open('example.txt', 'w') as file:
    # Write some text to the file
    file.write('Hello, World!\n')
    file.write('This is a new file created using Python.')

print("File has been created and text has been written.")
print("sahi hai na sab")
print("jassaajs")
print("sanamre")

      
file = open("example.txt", "r")
print(file.read())

with open("sallu.txt", "w") as mulla:
    mulla.write("bhai gadi driver chala raha tha\nisme meri kya galti")
print("sallu bhai ki file ban chuki hai")

import os
os.remove('sallu.txt')

print("END of the WORLDS")
print("END of the Games")
