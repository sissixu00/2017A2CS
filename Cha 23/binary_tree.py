#Sissi Xu S3C2
NP=-1
class Node:
    def __init__(self):
        self.Data=""
        self.LeftP=NP
        self.RightP=NP
def InitTree():
    Tree=[Node() for i in range (8)]
    RootP=NP
    FreeP=0
    for Index in range (7):
        Tree[Index].LeftP=Index+1
    return(Tree, RootP, FreeP)
def InsertNode(Tree, RootP, FreeP, NewItem):
    if FreeP != NP:
        NewNodeP=FreeP
        Tree[NewNodeP].Data = NewItem
        FreeP=Tree[FreeP].LeftP
        Tree[NewNodeP].LeftP=NP
        if RootP == NP:
            RootP = NewNodeP
        else:
            ThisNodeP = RootP
            while ThisNodeP != NP:
                PreNodeP = ThisNodeP
                if Tree[ThisNodeP].Data > NewItem:
                    TurnLeft = True
                    ThisNodeP = Tree[ThisNodeP].LeftP
                else:
                    TurnLeft = False
                    ThisNodeP = Tree[ThisNodeP].RightP
            if TurnLeft:
                Tree[PreNodeP].LeftP = NewNodeP
            else:
                Tree[PreNodeP].RightP = NewNodeP
    else:
        print("no space for more data")
    return(Tree, RootP, FreeP)
def FindNode(Tree, RootP, SearchItem):
    ThisNodeP = RootP
    while ThisNodeP != NP and Tree[ThisNodeP].Data != SearchItem:
        if Tree[ThisNodeP].Data > SearchItem:
            ThisNodeP = Tree[ThisNodeP].LeftP
        else:
            ThisNodeP = Tree[ThisNodeP].RightP
    return (ThisNodeP)
def TraverseTree(Tree, RootP):
    if RootP != NP:
        TraverseTree(Tree, Tree[RootP].LeftP)
        print(Tree[RootP].Data)
        TraverseTree(Tree, Tree[RootP].RightP)
def GetOption():
    print("1: add data")
    print("2: find data")
    print("3: traverse tree")
    print("4: end program")
    option = input("enter your choice:")
    return(option)
Tree, RootP, FreeP = InitTree()
Option = GetOption()
while Option != "4":
    if Option == "1":
        Data = input("enter the value:")
        Tree, RootP, FreeP = InsertNode(Tree, RootP, FreeP, Data)
        TraerseTree(Tree, RootP)
    elif Option == "2":
        Data = input("enter search value:")
        ThisNodeP = FindNode(Tree, RootP, Data)
        if ThisNodeP == NP:
            print("value not found")
        else:
            print("value found at", ThisNodeP)
        print(RootP, FreeP)
        for i in range (8):
            print(i, "", Tree[i].LeftP, "", Tree[i].Data, "", Tree[i].RightP)
    elif Option == "3":
        TraverseTree(Tree, RootP)
    Option = GetOption()
