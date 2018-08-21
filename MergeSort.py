#the inv variable counts the number of inversions. It's a cool exercise to see how many comparisons the computer made.

from random import *
#inp=open("text.txt", "r").readlines()
inp=[9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
#numbers = [x for x in range(0, 1000000)]
#numbers.reverse()
numbers=[6,5,4,3,2,1]
def inputing(path):
 #   inp = [int(x) for x in open(path, "r").readlines()]
    global inp
    def mergeSort(array,inv):
        if len(array)<=1:
            print(array)
            return 0
        else:
            midpoint = len(array)//2
            leftSide = array[:midpoint]
            rightSide= array[midpoint:]
            
            invL=mergeSort(leftSide,0)
            invR=mergeSort(rightSide,0)
            leftIndex=0
            rightIndex=0
            k=0
            #inv+= invL+invR
            while leftIndex<len(leftSide) and rightIndex<len(rightSide):
                if leftSide[leftIndex]<=rightSide[rightIndex]:#change the operator here to make the sort increasing or decreasing
                    array[k]=leftSide[leftIndex]
                    leftIndex+=1
                    k+=1
                else:#handles equality cases
                    array[k]=rightSide[rightIndex]
                    rightIndex+=1
                    k+=1
 #                   inv+=len(leftSide)-leftIndex
                    #print(len(leftSide)-leftIndex, inv)
            while leftIndex < len(leftSide):
                array[k]=leftSide[leftIndex]
                leftIndex+=1
                k+=1
                
            while rightIndex < len(rightSide):
                array[k]=rightSide[rightIndex]
                rightIndex+=1
                k+=1
 #               inv+=len(leftSide)-leftIndex
            #print(inv)
            return array
    return mergeSort(inp, 0)
print(inputing("text.txt"))
print("Done!")
