class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for ch in s:
            if ch.isalnum():
                newStr += ch.lower()
        if newStr[::-1] != newStr:
            return False
        else:
            return True