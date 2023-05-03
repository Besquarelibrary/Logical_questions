def sort(a, N):
	low = 0
	high = N - 1
	mid = 0
	while mid <= high:
		if a[mid] == 0:
			a[low], a[mid] = a[mid], a[low]
			low = low + 1
			mid = mid + 1
		elif a[mid] == 1:
			mid = mid + 1
		else:
			a[mid], a[high] = a[high], a[mid]
			high = high - 1
	return a
def printArray(a):
	for k in a:
		print(k, end=' ')
arr = [0,1,2,0,1]
N = len(arr)
arr = sort(arr, N)
printArray(arr)