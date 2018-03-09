#Sissi Xu S3C2
NullPointer = -1
class Node:
    def __init__(self):
        self.data = ""
        self.Pointer = NullPointer
    def InitialiseQ():
        Q = [Node() for i in range(8)]
        HeadOfQ = NullPointer
        EndOfQ = NullPointer
        FreeListPtr = 0
        for Index in range(7):
            Q[Index].Pointer = Index +1
        Q[7].Pointer = NullPointer
        return(Q, HeadOfQ, EndOfQ, FreeListPtr)
    def JoinQ(Q, HeadOfQ, EndOfQ, FreeListPtr, NewItem):
        if FreeListPtr != NullPointer:
            NewNodePtr = FreeListPtr
            Q[NewNodePtr].Data = NewItem
            FreeListPtr = Q[FreeListPtr].Pointer
            Q[NewNodePtr].Pointer = NullPointer
            if EndOfQ == NullPointer:
                HeadOfQ = NewNodePtr
            else:
                Q[EndOfQueue].Pointer = NewNodePtr
            EndOfQ = NewNodePtr
        else:
            print("no space for more data")
        return (Q, HeadOfQ, EndOfQ, FreeListPtr)
    def LeaveQ(Q, HeadOfQ, EndOfQ, FreeListPtr):
        if HeadOfQ != NullPointer:
            Value = Q[HeadOfQ].Data
            ThisNodePtr = Q[HeadOfQ].Pointer
            if ThisNodePtr == NullPointer:
                EndOfQ = NullPointer
            Q[HeadOfQ].Pointer = FreeListPtr
            FreeListPtr = HeadOfQ
            HeadOfQ = ThisNodePtr
        else:
            print("queue empty")
            Value = ""
        return (Q, HeadOfQ, EndOfQ, FreeListPtr, Value)
    def OutputAllNode(Q, HeadOfQ):
        CNodePtr = HeadOfQ
        if HeadOfQ == NullPointer:
            print("no data in list")
        while CNodePtr != NullPointer:
            print(CNodePtr, "", Q[CNodePtr].Data)
            CNodePtr = Q[CNodePtr].Pointer
    def GetOption():
        print("1: join queue")
        print("2: leave queue")
        print("3: output queue")
        print("4: end program")
        option = input ("Enter your choice:")
        return(option)
    Q, HeadOfQ, EndOfQ, FreeListPtr = InitialiseQ()
    Option = GetOption()
    while Option != "4":
        if Option == "1":
            Data = input("Enter the value:")
            Q, HeadOfQ, EndOfQ, FreeListPtr = JoinQ(Q, HeadOfQ, EndOfQ, FreeListPtr, Data)
            OutputAllNodes(Q, HeadOfQ)
        elif Option == "2":
            Q, HeadOfQ, EndOfQ, FreeListPtr, Value = LeaveQ(Q, HeadOfQ, EndOfQ, FreeListPtr)
            print("data leaving queue:", Value)
            OutputAllNodes(Q, HeadOfQ)
        elif Option == "3":
            OutputAllNodes(Q, HeadOfQ)
            print(HeadOfQ, EndOfQ, FreeListPtr)
            for i in range(8):
                print(i, "", Q[i].Data, "", Q[i].Pointer)
        Option = GetOption()
    
