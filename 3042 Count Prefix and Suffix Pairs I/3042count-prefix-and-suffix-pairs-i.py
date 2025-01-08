class Solution:

    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:

        if len(str1) <= len(str2):
            if str1 == str2[:len(str1)] and str1 == str2[-len(str1):]:
                return True
            else:
                return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                res = self.isPrefixAndSuffix(words[i], words[j])
                if res:
                    c+=1

        return (c)

        