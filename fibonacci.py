import LinkedList
import random

#Function used in Main()
def Print(Str, Stuff, Together = False):
    Str = str(Str)
    if isinstance(Stuff, LinkedList.LinkedList):
        print(Str + ": ")
        if Together == False:
            Stuff.Display()
        else:
            Stuff.Display(True)
        return
    print(Str + ": " + str(Stuff))

def Split(Number):
    StrNumber = str(Number)
    if len(StrNumber) > 10:
        N1 = int(StrNumber[0:-10])
        N2 = int(StrNumber[-10:])
        return N1, N2
    return 0, Number

def Sizing(L1, L2):
    while L1.Length() > L2.Length():
        L2.Insert(0, 0)
    while L2.Length() > L1.Length():
        L1.Insert(0, 0)
    return(L1, L2)

def AntiZero(Number):
    StrNumber = str(Number)
    while StrNumber[0] == "0" or StrNumber[0] == 0:
        StrNumber = StrNumber[1:]
    return int(StrNumber)

def ReturnZero(Number):
    if isinstance(Number, LinkedList.LinkedList):
        for i in range(Number.Length()):
            if i != 0:
                while len(str(Number.Get(i))) != 10:
                    Str = "0" + str(Number.Get(i))
                    Number.Insert(i, Str, True)
    else:
        while len(str(Number)) != 10:
            Number = "0" + str(Number)
    return Number

def Inserting(L1, L2, L3):
    if L1 != 0:
        if len(str(L3.Get(0, False))) < 10 and L3.Get(0, False) != None:
            L3.Insert(0, L2 + L3.Get(0), True)
            L3.Insert(0, L1)
        else:
            L3.Insert(0, L2)
            L3.Insert(0, L1)
    elif L1 == 0:
        if len(str(L3.Get(0, False))) < 10 and L3.Get(0, False) != None:
            L3.Insert(0, L2 + L3.Get(0), True)
        else:
            L3.Insert(0, L2)

    return L3

def Adding(L1, L2):
    L3 = LinkedList.LinkedList()
    L1, L2 = Sizing(L1, L2)

    L1Length = L1.Length()
    L2Length = L2.Length()

    for i in range(L1Length):     
        if L1.Get(L1Length - i - 1) != None and L2.Get(L2Length - i - 1) != None:         
            Number = L1.Get(L1Length - i - 1) + L2.Get(L2Length - i - 1) 
            #Number = ReturnZero(Number)
            
            SL1, SL2 = Split(Number)      

            if L1 != 0:
                if len(str(L3.Get(0, False))) < 10 and L3.Get(0, False) != None:
                    L3.Insert(0, SL2 + L3.Get(0), True)
                    L3.Insert(0, SL1)
                else:
                    L3.Insert(0, SL2)
                    L3.Insert(0, SL1)
            elif L1 == 0:
                if len(str(L3.Get(0, False))) < 10 and L3.Get(0, False) != None:
                    L3.Insert(0, SL2 + L3.Get(0), True)
                else:
                    L3.Insert(0, SL2)

    return L3

        
    
#Working Area

F1 = LinkedList.LinkedList()
F2 = LinkedList.LinkedList()
F3 = None

F1.Append(1)
F2.Append(1)

Number = 0
while Number < 500:
    F3 = Adding(F1, F2)
    F1Zero = ReturnZero(F1)
    F1Number = F1Zero.Display(True)
    F1Number = AntiZero(F1Number)
    print(F1Number)
    F1 = F2
    F2 = F3
    Number += 1



