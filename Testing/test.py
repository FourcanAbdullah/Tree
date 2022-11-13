import sys
import os


# def traversingThruRoot(directory):

#     sortedList = sorted(os.listdir(directory))

#     for elements in sortedList:
#         newpath = os.path.join(directory, elements)
#         print(newpath)
#         if (os.path.isdir(newpath)):
#             print(elements, "is a directory")
#             traversingThruRoot(newpath)


# directory = os.getcwd()
# print(directory)
# traversingThruRoot(directory)


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
                traversingThruRoot(newpath, prefix + "    ")
        else:
            print(prefix+"├───", sortedList[givenIndex])
            if (os.path.isdir(newpath)):
                traversingThruRoot(newpath, prefix + "│   ")


directory = os.getcwd()
current = directory
print(".")

traversingThruRoot(directory, '')
