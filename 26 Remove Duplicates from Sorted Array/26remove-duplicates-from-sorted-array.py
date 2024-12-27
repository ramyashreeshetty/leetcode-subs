class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # If the array is empty, return 0
            return 0

        i = 0  # Pointer for the position of the last unique element

        for j in range(1, len(nums)):  # Start iterating from the second element
            if nums[j] != nums[i]:  # Check if the current element is unique
                i += 1
                nums[i] = nums[j]  # Update the position of the next unique element

        return i + 1  # Number of unique elements (index + 1)

        