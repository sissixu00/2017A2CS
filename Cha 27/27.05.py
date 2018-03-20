# Sissi Xu S3C2

class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title=t
        self.__Author_Artist=a
        self.ItemID=i
        self.__OnLoan=False
        self.__DueDate=datetime.date.today()
        self.__BorrowerID=0

    def Borrowing(self,b):
        self.__OnLoan=True
        self.__DueDate=self.__DueDate + datetime.timedelta(weeks = 3)
        self.__BorrowerID=b

    def PrintDetails(self):
        print(self.__Title, ';', self.__Author__Artist, ';' end = '')
        print(self.__ItemID, ';', self.__OnLoan)
        print(self.__DueDate, ': Borrower;', self.__BorrowerID)
