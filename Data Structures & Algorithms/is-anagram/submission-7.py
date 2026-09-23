import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}
        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1
        for i in t:
            if i in t_hash:
                t_hash[i] += 1
            else:
                t_hash[i] = 1
        for c in s_hash:
            if s_hash[c] != t_hash.get(c,0):
                return False
        return True
        
