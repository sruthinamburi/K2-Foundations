#sorts a list in ascending order using selection sort strategy
list = [6,2,1,4,6,0]
length = len(list)
def selectionsort(list):
    for i in range (0, length-1):
        minval = i
        for j in range(i+1, length):
                if list[j] < list[minval]:
                    minval = j
        if minval!=i:
            list[i],list[minval] = list[minval],list[i]

selectionsort(list)
print(list)
