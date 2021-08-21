class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = ''.join(i for i in s if i.isalnum())
        d = d.lower()
        c = d
        d = d[::-1]
        if c == d:
            return True
        else:
            return False
