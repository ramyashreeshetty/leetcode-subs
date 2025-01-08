class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) -1 or flowerbed[i + 1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        return n <= 0












        # c = 0
        # if n == 0:
        #     return True
        # elif n == 1 and len(flowerbed) == 1 and flowerbed[0] == 0:
        #     return True

        # if flowerbed[0] == 0 and flowerbed[1] == 0:
        #     flowerbed[0] = 1
        #     c += 1
        #     if c >= n:
        #         return True

        # if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        #     flowerbed[-1] = 1
        #     c += 1
        #     if c >= n:
        #         return True

        # print(flowerbed)
        # for i in range(1, len(flowerbed)-1):
        #     if flowerbed[i] == 0:
        #         if flowerbed[i-1] == 1 or flowerbed[i+1] == 1:
        #             continue
        #         else:
        #             flowerbed[i] = 1
        #             c += 1
        #             if c >= n:
        #                 return True
        # print(c, flowerbed)
        # return False



        