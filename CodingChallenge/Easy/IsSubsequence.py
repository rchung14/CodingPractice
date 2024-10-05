class Solution(object):
    def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        sTrack = 0
        for i in t: 
            if s[sTrack] == i:
                sTrack += 1
            if sTrack == len(s):
                return True
        
        return False
    
    s = "abc"
    t = "aecbd"
    print(isSubsequence(s,t))
    