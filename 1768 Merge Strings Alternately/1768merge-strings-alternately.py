class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # if len(word2) < len(word1):
        #     wlen = len(word2)
        #     add_str = word1[wlen : len(word1)]
        #     word1 = word1[0 : wlen]           
        # else:
        #     wlen = len(word1)
        #     add_str = word2[wlen : len(word2)]
        #     word2 = word2[0 : wlen]

        # #print(word1, word2, wlen, add_str)

        # res = ''
        # for i in range(0, wlen):
        #     res = res + word1[i] + word2[i]
        # res = res + add_str
        
        # return res

        res = []
        for i in range(min(len(word1),len(word2))):
            res.append(word1[i] + word2[i])
            
        return ''.join(res) + word1[i+1:] + word2[i+1:]

