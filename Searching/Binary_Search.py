''' 
   Time-Complexcity is O(log(n)) beacause it deletes the list if data is less than or greater than mid
   Space-Complexcity is O(1)

 '''

def binary_search_iterative(data, target):
	low = 0
	high = len(data) - 1
	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False

def binary_search_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid-1)
		else:
			return binary_search_recursive(data, target, mid+1, high)

print(binary_search_iterative(data, 5))
