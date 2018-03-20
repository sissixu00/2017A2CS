# Sissi XuS3C2
class Assessment:
    def __init__(self, t, m):
        self.__assessmenttitle=t
        self.__maxmarks=m
    def outputassessmentdetails(self):
        print(self.__assessmenttitle, "Marks:", self.__maxmarks)
class Course:
    def __init__(self, t, m):
        self.__coursetitle=t
        self.__maxstudents=m
        self.__numberoflessons=0
        self.__courselesson=[]
        self.__courseassessment=assessment
    def addlesson(self, t, d,r):
        self.__numberoflessons = self.__numberoflessons + 1
        self.__courselesson.append(lesson(t, d, r))
    def addassessment(self, t, m):
        courseassessment = assessment(t, m)
    def outputcoursedetails(self):
        print(self.__coursetitle, end='')
        print("Maximum number of students:", self.__maxstudetns)
        for i in range(self.__numberoflessons):
print(self.__courselesson[i].outputlessondetails()
                  
class Lesson:
    def __init__(self, t, d, r):
        self.__lessontitle = t
        self.__durationminutes = d
        self.requireslab = r
    def outputlessondetails(self):
        print(self.__lessontitle, self.__durationminutes)
