class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store value and its index
        num_to_index = {}

        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], index]

            # Store the current number and its index
            num_to_index[num] = index

        # If no solution is found (not expected as per problem)
        return []