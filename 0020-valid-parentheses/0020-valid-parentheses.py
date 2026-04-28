class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(':')','[':']','{':'}'
        }
        for char in s :
            if char in mapping:
                stack.append (char)
            else:
                if not stack :
                    return False
                top = stack.pop()
                if mapping[top] != char:
                    return False
        return len(stack) == 0