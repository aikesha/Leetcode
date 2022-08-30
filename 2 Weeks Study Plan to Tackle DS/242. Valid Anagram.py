"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(s) == len(t):
            for i in t:
                if t.count(i) == s.count(i):
                    count += 1         
            return count == len(t)
        return False