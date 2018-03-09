# Sissi Xu S3C2
import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        
    def GetTitle(self):
        return(self.__Title)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Titel,';',self.__Author__Artist,';',end='')
        print(self.__ItemID,';',self.__OnLoan,';',self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem._init__(self, t, a, i)
        self.__IsRequusted= False
        self.__RequestedBy = 0
        
    def GetIsRequired(self):
        return(self.__IsRequested)

    def SetIsRequested(self):
        self.__IsRequested = True

class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ''

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self, g):
        self.__Genre = g

B = []
B.append(Book('12 Rules for Life','Jordan Peterson',12))
B.append(Book('White Fang','Jack London',30))
B.append(Book('Harry Potter','J.K.Rowling',54))
B.append(Book('Lord of the Rings','J.R.R.Tolkin',357))

C = []
C.append(CD('And Justice For All','Metallica',550))
C.append(CD('Dark Side of the Moon','Pink Floyd',774))
C.append(CD('Black Sabbath','Black Sabbath',99))
