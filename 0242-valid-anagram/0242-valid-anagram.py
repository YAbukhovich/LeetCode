class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letters1 = {}
        letters2 = {}
        for i in t:
            letters1[i] = letters1.get(i,0) + 1
        for j in s:
            letters2[j] = letters2.get(j,0) + 1 
        if letters1 == letters2:
                return True
        return False         


        