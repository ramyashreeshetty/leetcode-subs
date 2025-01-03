class Solution:
    def maxScore(self, s: str) -> int:
        sumZero = 0
        max_sum = 0
        sumOne = s.count('1')
        print(sumOne)

        if sumOne == 0:
            sumZero = s.count('0')
            return sumZero - 1


        for i in range(len(s) - 1):
            
            if s[i] == '0':
                sumZero += 1
            elif s[i] == '1':
                sumOne -= 1
            
            res = sumZero + sumOne
            print(i , res, '<-', sumZero, sumOne)
            max_sum = max(max_sum, res)
            
        
        return max_sum
        