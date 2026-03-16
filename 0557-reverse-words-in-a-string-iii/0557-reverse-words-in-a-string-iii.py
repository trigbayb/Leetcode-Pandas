class Solution:
    def reverseWords(self, s: str) -> str:
        s1=""
        for i in s.split():
            s1+=i[::-1]+" "
        return s1[:-1]
        