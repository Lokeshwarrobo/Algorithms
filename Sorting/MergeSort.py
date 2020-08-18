array = [10, 9, 8, 5, 6, 7, 1, 2, 3, 4]

def merge_sort(array):
	if len(array) == 1:
		return array
	mid = len(array) // 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	return merge(left, right)

def merge(left, right):

	result = []
	i = j = 0

	while (len(result) < (len(left)+len(right))):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break
	return result

print(merge_sort(array))
