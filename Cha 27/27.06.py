# Sissi Xu S3C2
class Book(LibraryItem):
    def __init__(self, t, a ,i):
        LibrryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.RequestedBy = 0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self, b):
        self.__IsRequested = True
        self.__RequestedBy = b
    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        if self.__IsRequested :
            print('Requested by', self.__RequestedBy)
        else:
            print('no requests')

    ThisBook.SetIsRequested(274)
    ThisBook.PrintDetails()
