from collections import Counter

class Solution(object):
    def isAnagram(self,s,t):
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    s = "listen"
    t = "silent"

    print(sol.isAnagram(s,t))
