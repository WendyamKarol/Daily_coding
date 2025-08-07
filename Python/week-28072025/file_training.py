"""with open("data/test1.txt","r") as file1 :
    file_stuff=file1.read
    print(file_stuff)
print(file1.closed)
print(file_stuff)"""

"""with open("data/test2.txt","r") as file:
    file_stuff=file.readline()
    print(file_stuff)
    file_stuff=file.readline()
    print(file_stuff)
    file_stuff=file.readline()
    print(file_stuff)"""

"""with open("data/test2.txt","r") as file :
    for line in file:
        print(line)"""

"""with open("data/test1.txt","r") as file:
    print("The first line of file : " + file.readline())
    """
#Iterate through the lines
"""with open("data/test2.txt","r") as file :
    i=0
    for line in file:
        print("Iteration", str(i), ":", line)
        i+=1"""

#Read all lines and save as a list
with open("data/test2.txt","r") as file:
    FileasList = file.readlines()
    print(FileasList)
