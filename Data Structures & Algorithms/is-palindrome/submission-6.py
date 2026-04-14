class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = ""

        for n in s:
            if n.isalnum():
                newstring += n.lower()

        return newstring == newstring[::-1]
