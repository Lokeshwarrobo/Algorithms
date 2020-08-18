array = [10, 9, 8, 6, 7, 5, 0, 1, 2, 3, 4]

def Insertion_Sort(array):
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j-1, array)
			j -= 1
	return array


def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

print(Insertion_Sort(array))

