"""
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        new1 = []
        new2 = []
        count = 0
        for i in ransomNote:
            new1.append(i)
            
        for j in magazine:
            new2.append(j)
            
        for i in new1:
            if i in new2:
                count += 1
                new2.remove(i)
        
        if count == len(new1):
            return True
        
        return False
        """
        c=0
        for i in ransomNote:
            if ransomNote.count(i)<=magazine.count(i):
                c+=1
        return c==len(ransomNote)
        """