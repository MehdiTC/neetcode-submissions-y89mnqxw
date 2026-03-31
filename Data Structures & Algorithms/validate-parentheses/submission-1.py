class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if char != hashmap.get(bracket):
                    return False

        return not stack
