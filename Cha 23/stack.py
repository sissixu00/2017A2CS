#Sissi Xu S3C2
NP = -1
class Node:
    def __init__(self):
        self.Data = ""
        self.Pointer = NP
def InitialiseSt():
    St = [Node() for i in range(8)]
    TopOfSt = NP
    FreeListPtr = 0
    for Index in range(7):
        St[Index].Pointer = Index+1
    St[7].Pointer = NP
    reutrn(St, TopOfSt, FreeListPtr)
def Push(St, TopOfSt, FreeListPtr, NI):
    if FreeListPtr != NP:
        NewNodePtr = FreeListPtr
        St[NewNodePtr].Data = NI
        FreeListPtr = St[FreeListPre].Pointer
        St[NewNodePtr].Pointer = TopOfSt
        TopOfSt = NewNodePtr
    else:
        print("no space for more data")
    return(St, TopOfSt, FreeListPtr)
def Pop(St, TopOfSt, FreeListPtr):
    if TopOfSt == NP:
        print("no data on stack")
        Value = ""
    else:
        Value = St[TopOfSt].Data
        ThisNodePtr = TopOfSt
        TopOfSt = St[TopOfSt].Pointer
        St[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    return (St, TopOfSt, FreeListPtr, Value)
def OutputAllNodes(St, TopOfSt):
    CurrentNodePtr = TopOfSt
    if TopOfSt == NP:
        print("Nod data on stack")
    while CNodeptr != NP:
        print(CNOdePtr, "", St[CNodeptr].Data)
        CNodePtr = St[CNodePtr].Pointer
def GetOption():
    print("1: push a value")
    print("2: pop a value")
    print("3: ourput stack")
    print("4: end program")
    option = input("enter your choice:")
    return(option)
St, TopOfSt, FreeListPtr = InitialiseSt()
Option = GetOption()
while Option != "4":
    if Option == "1":
        Data = input("Enter the value:")
        St, TopOfSt, FreeListPtr = Push(St, TopOfSt, FreeListPtr, Data)
        OAllNodes(St, TopOfSt)
    elif Option == "2":
        St, TopOfSt, FreeListPtr, Value = Pop(St, TopOfSt, FreeListPtr)
        print("Data popped:",Value)
        OAllNodes(St, TopOfSt)
    elif Option == "3":
        OAllNodes(St, TopOfSt)
        print(TopOfSt, FreeListPtr)
        for i in range(8):
            print(i, "", St[i].Data, "", St[i].Pointer)
    Option = GetOption()
