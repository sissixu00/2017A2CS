#Sissi Xu S3C2
def bubblesort(List):
    n=len(List)
    while n>0:
        for i in range (n-1):
            if List[i]>List[i+1]:
                List[i], List[i+1] = List[i+1], List[i]
        n-=1
    return List
