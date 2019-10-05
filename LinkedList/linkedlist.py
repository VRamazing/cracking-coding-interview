class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            if(temp.next == None):
                print(str(temp.data))
                break
            print(str(temp.data) + "->", end=" ")
            temp = temp.next

    def push(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data
        
    def insertAfter(self, prev_node_value, new_data):           
        currentIndex = self.head
        while(currentIndex.next):
            if(currentIndex.data == prev_node_value):
                new_node = Node(new_data)
                new_node.next = currentIndex.next
                currentIndex.next = new_node
                break
            currentIndex = currentIndex.next
        
        print("The given prev value does not exist in linked list")
       
    
    def append(self, new_data): 
        new_node = Node(new_data)
        if(self.head is None):
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def removeFirst(self):
        if(self.head is None):
            return
        current_head_node = self.head
        self.head = self.head.next
        current_head_node.data = None
        current_head_node.next = None

    def removeLast(self):
        if(self.head is None):
            return
        
        last = self.head.next
        second_last = self.head

        while(last.next):
            last = last.next
            second_last = second_last.next

        second_last.next = None
        last.data = None

    def removeNodeWithValue(self, value):
        if(self.head is None):
            return

        last = self.head.next
        before_last = self.head
        while(last.next):
            if(last.data == value):
                before_last.next = last.next
                last.data = None
            before_last = before_last.next
            last = last.next

    def getNthNode(self, index):
        if(self.head is None):
            return
        counter = 1
        last = self.head
        while(last.next):
            if(counter==index):
                print(last.data)
                break
            last = last.next
            counter+=1
    
    def getNthNodeFromEnd(self, index):
        counter = 1
        last = self.head
        while(last.next):
            counter+=1
            last = last.next
        
        lengthOfList = counter
        last = self.head
        counter=1
        while(last.next):
            if(counter==(lengthOfList + 1 - index)):
                print(last.data)
                break
            last = last.next
            counter+=1

    def getMiddleOfLinkedList(self):
        counter1 = 0
        last = self.head
        
        while(last.next):
            last = last.next
            counter1+=1

        counter2 = 0
        last = self.head
        while(last.next):
            if(counter2 == counter1//2):
                print(last.data)
                break
            last = last.next
            counter2+=1

    def getMiddleOfLinkedListSinglePass(self):
        last = self.head
        plast = self.head

        while(last.next):
            if(last.next.next != None):
                last = last.next.next
                plast = plast.next
            else:
                break

        print(plast.data)

    def checkLinkedListAPalindrome(self):
        #Loop through list and push to stack. 
        #pop out of stack and see if things is same. 

    def removeDuplicateFromUnsorted(self):
        # sort with merge sort

def checkLinkedListIntersect(ll1, ll2):
    pass
            
if __name__ == '__main__':
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.append(4)
    llist.push(0)
    llist.append(5)
    llist.insertAfter(1,6)
    llist.printList()
    llist.removeFirst()
    llist.printList()
    llist.removeLast()
    llist.printList()
    llist.removeNodeWithValue(6)
    llist.printList()
    llist.append(5)
    llist.printList()
    llist.getNthNode(2)
    llist.getNthNodeFromEnd(2)
    llist.append(6)
    llist.printList()
    llist.getMiddleOfLinkedListSinglePass()
    llist.getMiddleOfLinkedList()
