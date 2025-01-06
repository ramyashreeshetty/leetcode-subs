class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        prefix_arr = [0] * len(boxes)

        for i in range(0, len(boxes)):
            ops = 0
            for j, ball in enumerate(boxes):
                if i!=j and ball=='1':
                    ops = ops + abs((j+1) - (i+1))
            prefix_arr[i] = ops
            #print(prefix_arr)

        return prefix_arr

    



        