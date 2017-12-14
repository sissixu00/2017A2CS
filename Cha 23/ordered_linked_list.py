#Sissi Xu S3C2
NP = -1
class ListNode:
    def __init__(self):
        self.Data = ""
        self.Pointer = NP
def InitialiseList():
    List = [ListNode() for i in range(8)]
    StartP = nP
    FreeListP = 0
    for Index in range(7):
        List[Index].Pointer = Index + 1
    List[7].Pointer = NP
    return(List, StartP, FreeListP)
def InsertNode(List, StartP, FreeListP, NewItem):
    if FreeListP != NP:
        NewNodeP = FreeListP
        List[NewNodeP].Data = NewItem
        FreeListP = List[FreeListP].Pointer
        PreviousNodeP = NP
        ThisNodeP = StartP
        while ThisNodeP != NP and List[ThisNodeP].Data < NewItem:
            PreviousNodep = ThisNodeP
            ThisNodeP = List[ThisNodeP].Pointer
        if PreviousNodeP == NP:
            List[NewNodeP].Pointer = StartP
            StartP = NewNodeP
        else:
            List[NewNodeP].Pointer = List[PreviousNodeP].Pointer
            List[PreviousNodeP].Pointer - NewNodeP
    else:
        print("no space for more data")
    return(List, StartP, FreeListP)
def FindNode(List, StartP, DataItem):
    CNodeP = StartP
    while CNodeP != NP and List[CNodeP].Data != DataItem:
        CnodeP = List[CNodeP].Pointer
    return (CNodeP)
def DeleteNode(List, StartP, FreeListP, DataItem):
    ThisNodeP = StartP
    while ThisNodeP != NP and List[ThisNodeP].Data != DataItem:
        PreNodeP = ThisNodeP
        ThisNodeP = List[ThisNodeP].Pointer
    if ThisNodeP != NP:
        if ThisNodeP == StartP:
            StartP = List[StartP].Pointer
        else:
            List[PreNodeP].Pointer = List[ThisNodeP].Pointer
        List[ThisNodeP].Pointer = FreeListP
        FreeListP = ThisNodeP
    else:
        print("data does not exist in list")
    return(List, StartP, FreeListP)
def OutputNode(List, StartP):
    CNodeP = StartP
    if StartP == NP:
        print("no data in list")
    while CNodeP != NP:
        print(CurrentNodePtr, " ",List[CurrentNodePtr].Data)
        CurrentNodePtr = List[CurrentNodePtr].Pointer
def GetOption():
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output list")
    print("5: end program")
    option = input("enter your choice:")
    return(option)
List, StartP, FreeListP = InitialiseList()
Option = GetOption()
while Option != "5":
    if  Option == "1":
        Data = input("enter the value:")
        List, StartP, FreeListP, = InsertNode(List, StartP, FreeListP, Data)
        OutputNode(List, StartP)
    elif Option == "2":
        Data = input("enter the value:")
        List, StartP, FreeListP = DeleteNode(List, StartP, FreeListP, Data)
        OutputNode(List, StartP)
    elif Option == "3":
        Data = input("enter the value:")
        CNodeP = FindNode(List, StartP, Data)
        if CNodeP == NP:
            print("data not found")
        print(StartP, FreeListP)
        for i in range(8):
            print(i, "", List[i].Data, "", List[i].Pointer)
    elif Option == "4":
        OutputNode(List, StartP)
    Option = GetOption()
