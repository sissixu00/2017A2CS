# Sissi Xu S3C2

import datetime
class TBorrower:
    def __init__(self, n, e, i):
        self.__BorrowerName = n
        self.__EmailAddress = e
        self.__BorrowerID = i
        self.__ItemsOnLoan = 0
    def getBorrowerName(self):
        return(self.__BorrowerName)
    def getEmailAddress(self):
        return(self.__EmailAddress)
    def getBorrowerID(self):
        return(self.__BorrowerID)
    def getItemsOnLOan(self):
        return(self.__ItemsOnLoan)
    def updateItemsOnLoan(self, n):
        self.__ItemsOnloan = self.__ItemsOnLoan + n
    def printDetails(self):
        print(self.__BorrowerName, ';',self.__BorrowerID, ';', end='')
        print(self.__EmailAddress, ';', self.__ItemsOnLoan)
class TLibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__BorrowerID = 0
        self.__DueDate = datetime.date.today()
    def getTitle(self):
        return(self.__Title)
    def getAuthor_Artist(self):
        return(self.__Author_Artist)
    def getItemID(self):
        return(self.__ItemID)
    def getOnLoan(self):
        return(self.__OnLoan)
    def getBorrowerID(self):
        return(self.__BorrowerID)
    def getDueDate(self):
        return(self.__DueDate)
    def Borrowing(self, i, x):
        if x.getItemsOnLoan()<5:
            self.__OnLoan = True
            self._-BorrowerID = x.getBorrowerID()
            self.__DueDate = self.__DueDate + datetime.timedelta(weeks)
            x.updateItemsOnLoan(1)
        else:
            print("too many books on loan")
    def Returning(self, i, x):
        self.__OnLoan = False
        x.updateItemsOnLoan(-1)
    def printDetails(self):
        print(self.__Title, ';', self.__Author_Aritst, ';', end = '')
        print(self._-ItemID, ';', self.__OnLoan, ';', end = '')
        print(self.__BorrowerID, ';', self.__DueDate)
class TBook(TLibraryItem):
    def __init__(self, t, a, i):
        TLibraryItem._init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def getIsRequested(self):
        return(self.__IsRequested)
    def getRequestedBy(self):
        return(self.__RequestedBy)
    def RequestBook(self, i, x):
        self.__IsRequested = True
        self.RequestedBy = x.getBorrowerID()
    def printDetails(self):
        TLibraryItem.printDetails(self)
        print(self.__IsRequested, ';', self.__RequestedBy)
        
