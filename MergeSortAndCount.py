def mergeSortAndCount(array):
    if len(array)<2:
        return (array, 0)
    else:
        midPoint = len(array)//2
        leftArray=array[:midPoint]
        rightArray=array[midPoint:]
        left, x = mergeSortAndCount(leftArray)
        right, y = mergeSortAndCount(rightArray)
        newArray=[]
        leftIndex=0
        rightIndex=0
        inversionCount = x+y
        while leftIndex<len(left) and rightIndex<len(right):
            if left[leftIndex] <= right[rightIndex] :
                newArray.append(left[leftIndex])
                leftIndex+=1
            else:
                newArray.append(right[rightIndex])
                inversionCount+=len(left)-leftIndex
                rightIndex+=1
        if leftIndex<len(left):
            newArray+=left[leftIndex:]
        else:
            newArray+=right[rightIndex:]
        return newArray, inversionCount
print(mergeSortAndCount([1,2,3,4,5,6]))
