class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            
            res = res + strs[0][i]
        
        return res