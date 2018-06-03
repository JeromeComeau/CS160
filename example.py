'''Sample program for Assignment 8, CS 160
Written By: Gayathri Iyer
How to append to a list - in this case list of colors
and how to define a function'''

#function to create the list
def createList():
    myList = []
    return myList

#function to add values to the list
def fillList(myList):
    myList.append("Red")
    myList.append("Blue")
    color = input("Please enter a color: ")
    myList.append(color)
    return myList

#function to print the list
def printList(myList):
    for color in myList:
        print(color, " ")

#main function
def main():
    myList = createList()
    fillList(myList)
    printList(myList)

#call the main
main()
