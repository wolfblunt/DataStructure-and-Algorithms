def insertion_sort(nums):

	for i in range(len(nums)):

		j = i
		
		while j>0 and nums[j-1] > nums[j]:
			swap(nums,j,j-1)
			j= j-1

	return nums

def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp


if __name__ == '__main__':

	nums = [2,4,-1,-2,0,9,78,45,98,-4]
	insertion_sort(nums)
	print(nums)