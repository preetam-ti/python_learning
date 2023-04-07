#glob module in Python, with which we can perform file matching with a specific pattern by using it 
# inside a program.
import os, glob

os.chdir("D:/")

for file in glob.glob("Telus*"):
    print(file)

##https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/
