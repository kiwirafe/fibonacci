#A Basic Linked List

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Append(self, data):
        NewNode = Node(data)
        Current = self.head
        if Current == None:            
            self.head = NewNode
        else:
            while Current.next != None:
                Current = Current.next
            Current.next = NewNode
            NewNode.prev = Current

    def Length(self):
        Current = self.head
        Total = 0
        while Current != None:            
            Total += 1
            Current = Current.next
        return Total 

    def Display(self, together=False):
        ElementsNumber = 1
        CurrentNode = self.head
        Together = ""
        while CurrentNode != None:
            if together == False:
                print(ElementsNumber, ":", CurrentNode.data)
            else:
                Together = Together + str(CurrentNode.data)
            CurrentNode = CurrentNode.next            
            ElementsNumber += 1
        if together == True:
            return Together

    def Get(self,index, message=True):
        if index >= self.Length() or index < 0:
            if message == True:
                print("ERROR: 'Get' Index Out of Range!")
            return None
        CurrentIndex = 0
        CurrentNode = self.head
        while True:
            if CurrentIndex == index: return CurrentNode.data
            CurrentNode = CurrentNode.next
            CurrentIndex += 1

    def Erase(self, index, message=True):
        if index >= self.Length() or index < 0:
            if message == True:
                print("ERROR: 'Get' Index Out of Range!")
            return
        CurrentIndex = 0
        CurrentNode = self.head
        while True:
            PrevNode = CurrentNode.prev
            if CurrentIndex == index:
                if index == 0:
                    self.head = CurrentNode.next
                    if CurrentNode.next != None:
                        if CurrentNode.next.next == None:
                            self.head.next = None
                        else:
                            self.head.next = CurrentNode.next.next
                    return
                PrevNode.next = CurrentNode.next
                if CurrentNode.next != None:
                    CurrentNode = CurrentNode.next
                    CurrentNode.prev = PrevNode              
                return
            Temp = CurrentNode
            CurrentNode = CurrentNode.next
            CurrentNode.prev = Temp
            CurrentIndex += 1

    def Insert(self, index, data, Erase=False):
        if Erase == True:
            self.Erase(index)

        if index >= self.Length() or index < 0:
            return self.Append(data)
            
        CurrentNode = self.head
        CurrentIndex = 0
        while True:
            PrevNode = CurrentNode.prev
            if CurrentIndex == index: 
                NewNode = Node(data)
                if index == 0:
                    self.head = NewNode
                    NewNode.next = CurrentNode
                    NewNode.prev = None
                    return
                PrevNode.next = NewNode
                NewNode.prev = PrevNode
                NewNode.next = CurrentNode
                if CurrentNode != None:
                    CurrentNode.prev = NewNode
                return   
            Temp = CurrentNode
            CurrentNode = CurrentNode.next
            CurrentNode.prev = Temp
            CurrentIndex += 1
