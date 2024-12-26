class Solution:
    def isUgly(self, n: int) -> bool:

        # if(n <= 0):
        #     return false
        # if n>0 and n<=6:
        #     return True
        # if n>2:
        #     nlen = round(n/2) + 1
        #     for i in range(2, nlen):
        #         print(i)
        #         if n%i==0 and i!=2 and i!=3 and i!=5:
        #             print(i)
        #             return False

        if (n <= 0):
            return False
        if n>0 and n<=6:
            return True
        if n>6:    
            factors = [2, 3, 5]
            for i in factors:
                while n % i == 0:
                    n = n // i
            return n == 1
        else:
            return false

        