class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        letters = string.ascii_lowercase

        # Sweep Line!
        # forward would insert a [+1, -1] and backward inserts a [-1, +1] for the start and end+1 positions.

        prefix_diff = [0] * (len(s) + 1)
        print(prefix_diff)

        # If the direction is forward, then the start is +1 and end+1 is -1, vice versa if it is backwards.
        for start, end, d in shifts:
            prefix_diff[end + 1] += -1 if d else 1
            prefix_diff[start] += 1 if d else -1
        
        # Prefix sum
        for i in range(1, len(prefix_diff)):
            prefix_diff[i] += prefix_diff[i-1]

        # Shift the chars
        res = ''
        for index, i in enumerate(s):
            idx = letters.find(i)
            n_idx = (idx + prefix_diff[index]) % 26
            #print(idx, prefix_diff[index], n_idx)
            res = res + letters[n_idx]
    
        return res


        


  