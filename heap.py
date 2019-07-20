def heapify(arr , n,i):

	largest = i
	leftChild = 2*i + 1
	rightChild = 2*i + 2

	if leftChild < n and arr[i] < arr[leftChild]:
		largest = leftChild

	if rightChild < n and arr[largest] < arr[rightChild]:
		largest = rightChild

	if largest != i:
		arr[i] , arr[largest] = arr[largest] , arr[i]

		heapify(arr , n , largest)


def heapSort(arr):

	n = len(arr)
	for i in range(n,-1,-1):
		heapify(arr , n , i)

	for i in range(n-1, 0 , -1):

		arr[i] , arr[0] = arr[0] , arr[i]
		heapify(arr, i , 0)



arr = [100,2,56,23,12,58,-4,99,-87,-65,19,20]
heapSort(arr)
n = len(arr)
#print(n)
print ("Sorted array is") 
for i in range(n): 
	print ("%d" %arr[i]), 
