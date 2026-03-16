class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest=""
        counter=0
        left=0
        right=0
        while left<(len(s)-1):
            while right<len(s):
                lg=""
                flag=False
                for j in s[left:(right+1)]:
                    if (j.upper() in s[left:(right+1)] and j.lower() in s[left:(right+1)]) is False:
                        flag=True
                        break
                if flag is not True and len(s[left:(right+1)])>counter:
                    longest=s[left:(right+1)]
                    counter=len(longest)
                right+=1
            right=left+1
            left+=1
        return longest