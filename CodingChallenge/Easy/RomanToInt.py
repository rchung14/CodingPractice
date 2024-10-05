class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0 

        for idx in range(len(s)): 
            if idx < len(s) - 1 and m[s[idx]] < m[s[idx+1]]: 
                ans -= m[s[idx]]
            else: 
                ans += m[s[idx]]
        
        return ans

    s = 'ILVMD'
    print(romanToInt(s))