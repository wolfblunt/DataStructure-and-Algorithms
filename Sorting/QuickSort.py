def quick_sort(nums , low , high):

	if low >= high:
		return

	pivot_index = partition(nums, low, high)
	quick_sort(nums, low, pivot_index-1)
	quick_sort(nums, pivot_index+1, high)

def partition(nums, low, high):

	pivot_index = (low + high)//2
	swap(nums, pivot_index, high)

	i = low

	for j in range(low, high,1):
		if nums[j] <= nums[high]:
			swap(nums,i,j)
			i+=1

	swap(nums, i, high)

	return i

def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp


if __name__ == "__main__":

	nums = [-4,-5,1,34,23,0,8,-6,9,10,12]
	quick_sort(nums, 0, len(nums)-1)
	print(nums)

