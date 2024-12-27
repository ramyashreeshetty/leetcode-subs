class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        if len(s) % 2 == 0:
            for char in s:
                if char in bracket_map.values():  # If it's an opening bracket
                    stack.append(char)
                elif char in bracket_map:  # If it's a closing bracket
                    if not stack or stack.pop() != bracket_map[char]:
                        return False
                else:
                    return False  # Invalid character
        else:
            return False

        return not stack  # Stack should be empty if valid

        # for i in range(len(s)):
        #     s = s.replace('{}', '').replace('[]', '').replace('()', '')
        # return s == ''
        