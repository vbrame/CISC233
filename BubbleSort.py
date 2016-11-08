
def bubbleSort(alist):
    #numIter = 0
    for iteration in range(len(alist)-1, 0, -1):
        for i in range(iteration):
            swap = True
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                swap = False
            #numIter += 1
            #print numIter, alist   #Print the current iteration number and the current list order

        if swap:
            #print "STOP"   #Inform the user that the program stopped early
            break

x = [2,1,4,8,6,7]
bubbleSort(x)
print x