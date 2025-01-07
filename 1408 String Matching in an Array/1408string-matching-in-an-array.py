class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = sorted(words, key=lambda x: len(x))
        print(arr)
        
        res = []
        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                if arr[i] in arr[j]:
                    print('res', arr[i])
                    res.append(arr[i])
                    break
        return res