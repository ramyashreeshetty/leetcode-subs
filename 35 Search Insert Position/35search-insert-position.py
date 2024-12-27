class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = 0
        if target in nums:
            return nums.index(target)

        if target > nums[-1]:
            return len(nums)
        
        if target < nums[0]:
            return 0

        for i in range(0,len(nums)):
            if nums[i] < target and nums[i+1] > target:
                return i + 1
            else:
                i += 1


        