class Solution(object):
    from collections import Counter
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i 
            
        return -1
