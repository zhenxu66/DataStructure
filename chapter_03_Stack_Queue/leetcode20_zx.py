# good in time, not good in memory
class Solution(object):
    def isValid(self, s: str) -> bool:
        leftG = '({['
        rightG = ')}]'

        stack = []
        for char in s:
            if char in leftG:
                stack.append(char)
            if char in rightG:
                if not stack:
                    return False
                stacktop = stack.pop()
                if char == ')' and stacktop != '(':
                    return False
                if char == ']' and stacktop != '[':
                    return False
                if char == '}' and stacktop != '{':
                    return False
                # else:
                #    return False
        return stack == []

if __name__ == '__main__':


    input_str1 = '[{(())}]'

    Solution1 = Solution()
    print(Solution1.isValid(input_str1))

    input_str1 = '(]'
    print(Solution1.isValid(input_str1))

