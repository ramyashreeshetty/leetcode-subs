class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = sum(nums)
        print('Len & Sum of arr ->',n, arr_sum,'\n')

        if n == 2:
            if nums[0] > nums[1]:
                return 1
            elif nums[0] == nums[1]:
                return 1
            else:
                return 0

        t = 0
        n_sum = arr_sum
        count = 0

        for i in range(0, n-1): # skip last element
            t = t + nums[i]
            n_sum = n_sum - nums[i]
            #print(t, n_sum)

            if t >= n_sum:
                count+=1
                #print('valid split', count)

        return count


        