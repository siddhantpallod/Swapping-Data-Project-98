import os

def swap():
    folder1 = input("Enter The First Folder Name: ")
    folder2 = input("Enter The Second Folder Name: ")

    with open (folder1, 'r') as a:
        dataA = a.read()

    with open (folder2, 'r') as b:
        dataB = b.read()

    with open (folder1, 'w') as a:
        a.write(dataB)

    with open (folder2, 'w') as b:
        b.write(dataA)


swap()
