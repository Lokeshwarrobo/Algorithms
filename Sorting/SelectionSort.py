array = [10, 9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
'''

Time Complexcity O(n^2)

Auxcilary Space  O(1)

'''
def Selection_Sort(array):
	curindex = 0
	while curindex < len(array)-1:
		smallindex = curindex
		for i in range(curindex + 1, len(array)):
			if array[smallindex] > array[i]:
				smallindex = i
		array[curindex], array[smallindex] = array[smallindex], array[curindex]
		curindex += 1
	return array
print(Selection_Sort(array))
