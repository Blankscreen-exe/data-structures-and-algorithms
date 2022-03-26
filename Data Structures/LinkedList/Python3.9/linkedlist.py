"""
Repository link: https://github.com/Blankscreen-exe/data-structures-and-algorithms
Repository Owner: Blankscreen-exe
You will find more datastructures and algorithms where this came from.
All of these are implemented using multiple languages
"""

"""Node class is for each node in
your linked list"""
class Node:
    #initializing 
    def __init__(self,data):
        self.data = data    #data stored in the node
        self.next = None    #pointer directing to next node

"""This class is for arranging each node
and assigning a header for the list"""
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
            print("\nERROR: There is no list to start with!")

    #this method is used to INSERT a node at
    #the start of an existing list
    def replaceHeader(self, new_data):
        #creates a new_node variable which
        #stores a Node class instance containing
        #the data which you want to put inside the new_node
        new_node = Node(new_data)
        #sets the new_node pointer to 
        #the existing header node
        new_node.next = self.head
        #sets the new_node as the
        #current header node
        self.head = new_node

        #printing a message for successfully completing the operation
        print("\nMESSAGE: Successfully finished replacing the header node with a new node")

    #this method is used to INSERT a node
    #anywhere in the middle of the list
    def insertAfter(self, prev_node, new_data):
        #checking if the given previous node
        #exists within the list or not
        #the function will stop if previous
        #node is found to be non-existent(None)
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        #creates a new_node variable which
        #stores a Node class instance containing
        #the data which you want to put inside the new_node
        new_node = Node(new_data)
        #sets the new_node pointer to 
        #what the existing previous node's
        #pointer had
        new_node.next = prev_node.next
        #sets the prev_node pointer to 
        #the inserted new node
        prev_node.next = new_node

        #printing a message for successfully completing the operation
        print("\nMESSAGE: Successfully finished inserting a new node after a selected node")

    #this method is used to INSERT a node
    #after the last node of the list
    def addTrailer(self, new_data):
        #creates a new_node variable which
        #stores a Node class instance containing
        #the data which you want to put inside the new_node
        new_node = Node(new_data)
        #checking if there are no elements inside the list already.
        #this means that the trailer we want to add is just the header node
        if self.head is None:
            self.head = new_node
        else:
            #obtaining the existing last node
            #by iterating through the list
            last_node = self.head
            while(last_node.next):
                last_node = last_node.next
            #setting last node's pointer to
            #our new node
            last_node.next = new_node

        #printing a message for successfully completing the operation
        print("\nMESSAGE: Successfully finished inserting a new node after the trailer node")

    #this method is used to DELETE a node
    #at any point of the list
    #containing the data which matches the input
    #this makes the very first occurence of such node to be deleted
    def deleteNodeByData(self, data_to_delete):
        #creatnig a temporary variable to
        #store the current header node
        temp = self.head
        #Checking if the header node is not empty
        #and that the "header's data" matches the "data to be deleted"
        if (temp is not None) and (temp.data == data_to_delete):
            #assigning current header's next list item to
            #be the new header
            self.head = temp.next
            #setting the current header to None
            #in other words deleting it from existence
            temp = None
        else:
            #searching for the data to be deleted
            #using linear search
            #also keeping track of the prev_node
            while temp is not None:
                if temp.data == data_to_delete:
                    break
                prev_node = temp
                temp = temp.next

            #prints a message if the data to be deleted
            #was not found within the list
            if temp == None:
                print(f"\nMESSAGE: Could not find the data \"{data_to_delete}\" in the list")
                return

            #unlinking the node from the list
            #here the "temp" is the node which
            #matched the search criteria
            prev_node.next = temp.next
            #setting the current header to None
            #in other words deleting it from existence
            temp = None
            #printing a message for successfully completing the operation
            print(f"\nMESSAGE: Successfully deleted \"{data_to_delete}\" in the list")

    #this method is used to DELETE a node
    #at any point of the list
    #containing the index number
    #the list is considered 0-indexed
##    def deleteNodeByIndex(self, index_to_delete):
##        #creatnig a temporary variable to
##        #store the current header node
##        temp = self.head
##        #Checking if the header node is not empty
##        #and that the "header's data" matches the "data to be deleted"
##        if (temp is not None) and (temp.data == data_to_delete):
##            #assigning current header's next list item to
##            #be the new header
##            self.head = temp.next
##            #setting the current header to None
##            #in other words deleting it from existence
##            temp = None
##        else:
##            #searching for the index to be deleted
##            #using linear search
##            #also keeping track of the prev_node
##            while temp is not None:
##                if temp.data == data_to_delete:
##                    break
##                prev_node = temp
##                temp = temp.next

"""calling the main method.
not needed when using this file as a module
this method diplays the use case"""
if __name__=='__main__':
 
    # created an empty list with no header node
    myllist = LinkedList()
    #Sets the header node
    myllist.head = Node("Mydata 1")
    #creating more un-linked modes
    second_node = Node("Mydata 2")
    third_node = Node("Mydata 3")
    fourth_node = Node("Mydata 4")

    #setting a pointer for the first node
    #referenced to second node
    myllist.head.next = second_node;
    
    #setting a pointer for the second node
    #referenced to third node
    second_node.next = third_node;

    #setting a pointer for the third node
    #referenced to fourth node
    third_node.next = fourth_node;

    #printing the whole list to stdout
    myllist.printMyList()

    #inserting a node at the very beginning of the list
    myllist.replaceHeader("Newdata 1")

    #printing the whole list to stdout
    myllist.printMyList()

    #inserting a node in the middle of the list
    myllist.insertAfter(second_node,"Newdata 2")

    #printing the whole list to stdout
    myllist.printMyList()

    #inserting a node at the end of the list
    myllist.addTrailer("Newdata 3")

    #printing the whole list to stdout
    myllist.printMyList()

    #deleting a node containing the passed data
    myllist.deleteNodeByData("Mydata 3")

    #printing the whole list to stdout
    myllist.printMyList()
