import math
class Solution:
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 == str2 + str1:
            #gcd_len = math.gcd(len(str1), len(str2))
            
            l1 = len(str1)
            l2 = len(str2)
            while l2 != 0:
                l1, l2 = l2, l1 % l1
            l3 = l1
            
            return str1[:l3]
        else:
            return ""
    


s1 = Solution()
print(s1.gcdOfStrings("abcabcabc", "abcab"))