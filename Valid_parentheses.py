class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen_mp = { ")":"(", "]":"[", "}":"{" }

        for c in s:
            if c in closeToOpen_mp:
                if stack and stack[-1] == closeToOpen_mp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
