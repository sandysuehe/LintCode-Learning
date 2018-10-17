def removeDuplicates(nums):
    if len(nums) in (0, 1):
        return len(nums)

    i = 1
    j = 1

    while j < len(nums):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i

nums = [1,1,2]
print removeDuplicates(nums)
