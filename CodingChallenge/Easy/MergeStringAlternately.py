class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) < len(word2): 
            shorterStr = word1
            longerStr = word2
        else: 
            shorterStr = word2
            longerStr = word1

        finalStr = ''
        
        for idx in range(len(shorterStr)): 
            finalStr += word1[idx]
            finalStr += word2[idx]
        
        finalStr += longerStr[len(shorterStr):]
        return finalStr
