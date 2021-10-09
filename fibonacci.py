import LinkedList

#Function used in Main()

# Styled print
def Print(Str, Stuff, Together = False):
    Str = str(Str)
    if isinstance(Stuff, LinkedList.LinkedList):
        print(Str + ": ")
        if Together == False:
            Stuff.Display()
        else:
            Stuff.Display(True)
    else:
        print(Str + ": " + str(Stuff))

# Add zeros to the front so two lists have the same size
def Sizing(L1, L2):
    MaxLen = max(L1.Length(), L2.Length())
    while L2.Length() < MaxLen:
        L2.Insert(0, 0)
    while L1.Length() < MaxLen:
        L1.Insert(0, 0)
    return(L1, L2)


def Adding(L1, L2, NumInList=100):
    L3 = LinkedList.LinkedList()
    L1, L2 = Sizing(L1, L2)

    ListLength = L1.Length()
    Plus1 = False

    for i in range(ListLength):     
        number = L1.Get(ListLength - i - 1) + L2.Get(ListLength - i - 1)
        
        if Plus1:
            L3.Insert(0, int(str(number)[-NumInList:]) + 1)
        else:
            L3.Insert(0, int(str(number)[-NumInList:]))

        if len(str(number)) > NumInList:
            Plus1 = True
        else:
            Plus1 = False

    if Plus1:
        L3.Insert(0, 1)
    return L3

#Working Area
F1 = LinkedList.LinkedList()
F2 = LinkedList.LinkedList()
F3 = None

F1.Append(1)
F2.Append(1)

number = 10000
for n in range(3, number + 1):
    F3 = Adding(F1, F2)
    Print(n, F3.Display(True))
    F1 = F2
    F2 = F3
