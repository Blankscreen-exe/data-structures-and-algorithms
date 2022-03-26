"""
Repository link: https://github.com/Blankscreen-exe/data-structures-and-algorithms
Repository Owner: Blankscreen-exe
You will find more datastructures and algorithms where this came from.
All of these are implemented using multiple languages
"""

"""Node class is for each node in your linked list"""
class Node:
    #initializing 
    def __init__(self,data):
        self.data = data    #data stored in the node
        self.next = None    #pointer directing to next node

"""This class is for arranging each node and assigning a header for the list"""
class LinkedList:
    #initializing
    def __init__(self):
        self.head = None    #attribute which stores the reference to the header node

    #This method prints the linked list by using the self.head attribute
    def printMyList(self):
        #getting the header node in the list
        temp = self.head

        #checking if the list contains any nodes or not
        #It prints an error message if there are zero node present
        if temp:
            while (temp):
                
                connector = "-->"
                if temp.next == None:
                    connector = ""
                    
                #printing the data stored in the current node
                print(f" {temp.data} {connector}",end="")
                #getting the next node and assigning it to "temp" variable
                temp = temp.next
            
        else:
            print("ERROR: There is no list to start with!")


"""calling the main method.
not needed when using this file as a module
this method diplays the use case"""
##if __name__=='__main__':
## 
##    # created an empty list with no header node
##    myllist = LinkedList()
##    #Sets the header node
##    myllist.head = Node("Mydata 1")
##    #creating more un-linked modes
##    second_node = Node("Mydata 2")
##    third_node = Node("Mydata 3")
##    fourth_node = Node("Mydata 4")
##
##    #setting a pointer for the first node
##    #referenced to second node
##    myllist.head.next = second_node;
##    
##    #setting a pointer for the second node
##    #referenced to third node
##    second_node.next = third_node;
##
##    #setting a pointer for the third node
##    #referenced to fourth node
##    third_node.next = fourth_node;
##
##    #printing the whole list to stdout
##    myllist.printMyList()
