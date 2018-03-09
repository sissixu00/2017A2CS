# Sissi Xu S3C2

def PrintDetails(self):
    print("book details")
    LibraryItem.PrintDetails(self)
    print(self.__IsRequested)

def PrintDetails(self):
    print("CD details")
    LibraryItem.PrintDetails(self)
    print(self.__Genre)
