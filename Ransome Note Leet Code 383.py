from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True
sol = Solution()
print(sol.canConstruct("a","b"))
print(sol.canConstruct("aa","ab"))
print(sol.canConstruct("aa","aab"))

# Time Complexity	O(n + m)
# Space Complexity	O(1)