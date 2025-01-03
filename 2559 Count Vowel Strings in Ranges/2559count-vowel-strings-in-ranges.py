class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        cnt = []
        vow = 'aieou'
        prefix_arr = [0] * (len(words) + 1)

        for index, word in enumerate(words):
            if word[0] in vow and word[-1] in vow:
                prefix_arr[index + 1] = prefix_arr[index] + 1
            else:
                prefix_arr[index + 1] = prefix_arr[index]
        
        #print(prefix_arr)

        for query in queries:
            fIdx = query[0]
            lIdx = query[1] + 1

            res = prefix_arr[lIdx] - prefix_arr[fIdx]
            cnt.append(res)
        
        return cnt

            
                       
