array = [8, 5, 2, 3, 5, 9, 6]
'''
Time Complexcity   : Best case : O(nlog(n)), Worst case  : O(n2)

Space Complexcity  : O(nlog(n))

'''
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, startindex, endindex):
    if startindex >= endindex:
        return
    pivotindex = startindex
    leftindex = startindex + 1
    rightindex = endindex

    while rightindex >= leftindex:

        if array[leftindex] > array[pivotindex] and array[rightindex] < array[pivotindex]:
            array[leftindex], array[rightindex] = array[rightindex], array[leftindex]
        if array[leftindex] <= array[pivotindex]:
            leftindex += 1
        if array[rightindex] >= array[pivotindex]:
            rightindex -= 1

    array[pivotindex], array[rightindex] = array[rightindex], array[pivotindex]
    leftSubarrayisSmaller = rightindex - 1 -startindex < endindex - (rightindex + 1)

    if leftSubarrayisSmaller:
        quickSortHelper(array, startindex, rightindex-1)
        quickSortHelper(array, rightindex+1, endindex)
    else:
        quickSortHelper(array, rightindex+1, endindex)
        quickSortHelper(array, startindex, rightindex-1)


print(quickSort(array))
