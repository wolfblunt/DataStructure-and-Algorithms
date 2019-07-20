def merge_sort(nums):

	if len(nums) == 1:
		return

	middle_index = len(nums) // 2

	left_half = nums[:middle_index]
	right_half = nums[middle_index:]

	merge_sort(left_half)
	merge_sort(right_half)


	i = 0
	j = 0
	k = 0

	while i< len(left_half) and j < len(right_half):

		if left_half[i] < right_half[j]:
			nums[k] = left_half[i]
			i+=1

		else:
			nums[k] = right_half[j]
			j+=1

		k+=1

	while i < len(left_half):
		nums[k] = left_half[i]
		k+=1
		i+=1

	while  j < len(right_half):
		nums[k] = right_half[j]
		k+=1
		j+=1


if __name__ == "__main__":

	nums = [23,45,12,34,-12,-34,78,65,-74,-65,1,4,0]
	merge_sort(nums)
	print(nums)