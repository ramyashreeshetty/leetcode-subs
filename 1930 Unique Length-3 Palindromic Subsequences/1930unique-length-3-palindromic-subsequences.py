class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        char = set(s)

        for mid in char:
            first = s.find(mid)
            last = s.rfind(mid)

            if last > first - 1:
                unique = set(s[first+1:last])
                res += len(unique)

        return res










        # p_dict={}

        # for i in range(len(s)):
        #     left = s[i]

        #     for j in range(i+2, len(s)):
        #         if left == s[j] and left not in p_dict.keys():
        #             p_dict[left] = list(set(s[i+1:j]))

        #         elif left == s[j] and left in p_dict.keys():
        #             p_dict[left] = list(set(p_dict[left] + list(set(s[i+1:j]))))

        # res = 0
        # for i,v in p_dict.items():
        #     res = res + len(v)           

        # print(p_dict)
        # return res




        