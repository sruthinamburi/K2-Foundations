#sorts list in ascending order
list = [5,7,2,4,5,6,0,1]
def bubblesort(list):
    length = len(list)-1
    for i in range(0, length):
            for j in range(0, length-i):
                if list[j] > list[j+1]:
                 list[j], list[j+1] = list[j+1], list[j]
                 print (list)

bubblesort(list)
