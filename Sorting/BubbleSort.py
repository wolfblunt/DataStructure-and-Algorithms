def bubble_sort(nums):

	for i in range(len(nums)-1):
		for j in range(0,nums-1-i,1):
			if nums[j] > nums[j+1]:
				swap(nums, j ,j+1)

	return nums


def swap(nums, i ,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

if __name__ == '__main__':

	nums = [12,34,23,1,5,0,56,22,-1,-56,-34,88,97,57]
	bubble_sort(nums)
	print(nums)