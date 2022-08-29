"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        new_s=set(s)
        for i in s:
            if i in new_s:
                new_s.remove(i)
                if s.count(i) == 1:
                    return s.index(i)  
        return -1
        """
        for i in s:
            if s.count(i) == 1:
                return s.index(i)  
        return -1
        """