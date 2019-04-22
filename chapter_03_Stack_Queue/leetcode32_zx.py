class Solution:
    def longestValidParentheses(self, s: str) -> int:

        """
                :type s: str
                :rtype: int
                """
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    continue
            stack.append(i)
        max_length = 0
        next_index = len(s)
        while stack:
            cur_index = stack.pop()
            cur_length = next_index - cur_index - 1
            max_length = max(max_length, cur_length)
            next_index = cur_index
        max_length = max(max_length, next_index)
        return max_length


if __name__ == '__main__':

    input_str1 = '()())))'

    Solution1 = Solution()
    print(Solution1.longestValidParentheses(input_str1))

    input_str1 = '))))()'
    print(Solution1.longestValidParentheses(input_str1))
