class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        string_a = {}
        for a in s:
            string = a
            string_a[string] = string_a.get(a, 0) + 1

        string_b = {}
        for b in t:
            string = b
            string_b[string] = string_b.get(b, 0) + 1

        for a in string_a:
            if not string_a.get(a) == string_b.get(a):
                return False

        return True