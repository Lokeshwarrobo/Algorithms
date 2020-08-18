array = [10,9,8,7,6,5,5,4,3,2,1,0]

'''

Time Complexcity is O(n^2)
Auxilary Space is O(1)

'''
def Bubble_Sort(array):
	isSorted = False
	while not isSorted:    #O(n)
		isSorted = True
		for i in range(len(array) - 1): #O(n)
			if array[i] > array[i+1]:
				array[i],array[i+1] = array[i+1],array[i]
				isSorted = False
	return array
print(Bubble_Sort(array))
