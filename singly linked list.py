#singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

obj1 = Node(20)
obj2 = Node(30)
obj3 = Node(40)
obj4 = Node(50)
obj5 = Node(60)
obj6 = Node(70)
obj7 = Node(80)
obj8 = Node(90)
obj9 = Node(100)
obj10 = Node(110)

obj1.next = obj2
obj2.next = obj3
obj3.next = obj4
obj4.next = obj5
obj5.next = obj6
obj6.next = obj7
obj7.next = obj8
obj8.next = obj9
obj9.next = obj10

curr = obj1
while curr != None:
    print(curr.data, end = "-->")
    curr = curr.next

    

output:

20-->30-->40-->50-->60-->70-->80-->90-->100-->110-->


#Inserting a Node At End of The Tail

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end ="-->")
        curr = curr.next
    else:
        print("None")
    print()
 
def insertAtEndOfTail(head,ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newBlock
    return head
    

l = [11,22,33,44,55,66,77,88,99,110]
head = None
for ele in l:
    head = insertAtEndOfTail(head,ele)
printLinkedList(head)
 
output:
   
11-->22-->33-->44-->55-->66-->77-->88-->99-->110-->None

#Inserting a Node at head of linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end ="-->")
        curr = curr.next
    else:
        print("None")
    print()
 
def insertAtEndOfTail(head,ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newBlock
    return head

def insertNodeAtHeadOfLinkedList(head,ele):
    newBlock =Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head
    return newBlock


l = [11,22,33,44,55,66,77,88,99,110]
head = None
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head,ele)
printLinkedList(head)
    
output:

110-->99-->88-->77-->66-->55-->44-->33-->22-->11-->None

#Inserting a Node at Specific position

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def insertNodeAtHeadOfLinkedList(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
 
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head, ele)
 
printLinkedList(head)
head = insertAtSpecificPosition(head, 1, 1009)
printLinkedList(head)
 
output:

110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> 
1009 --> 110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> 


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def insertNodeAtHeadOfLinkedList(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
 
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head

def deleteTailNode(head):
    curr = head
    previous = None
    while curr.next != None:
        previous = curr
        curr = curr.next
    previous.next = None
    return head

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head, ele)
 
printLinkedList(head)
#head = insertAtSpecificPosition(head, 1, 1009)
head = deleteTailNode(head)
printLinkedList(head)
head = deleteTailNode(head)
printLinkedList(head)
 
output:

110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> 
110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 
110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 

