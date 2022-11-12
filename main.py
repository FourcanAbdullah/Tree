import sys
import os


def traversingThruRoot(directory, prefix):
    sortedList = sorted(os.listdir(directory))
    length = len(sortedList)
    if (directory != current):
        prefix = prefix+'     '
    for givenIndex in range(0, length, 1):
        newpath = os.path.join(directory, sortedList[givenIndex])
        if givenIndex == (length - 1):
            print(prefix+"└───", sortedList[givenIndex])
            if (os.path.isdir(newpath)):
                traversingThruRoot(newpath, prefix)
        else:
            print(prefix+"├───", sortedList[givenIndex])
            if (os.path.isdir(newpath)):
                traversingThruRoot(newpath, prefix)


directory = os.getcwd()
current = directory
print(".")

traversingThruRoot(directory, '')
