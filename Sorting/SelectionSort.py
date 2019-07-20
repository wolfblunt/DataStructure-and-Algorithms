def selection_sort(nums):

	for i in range(len(nums)-1):
		index = i

		for j in range(i+1,len(nums),1):
			if nums[j] < nums[index]:
				index = j

		if index != i:
			swap(nums,index,i)

	return nums


def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

if __name__ == '__main__':
	
	nums = [32,23,1,4,-6,-9,43,99,-100,33,100]
	selection_sort(nums)
	print(nums)