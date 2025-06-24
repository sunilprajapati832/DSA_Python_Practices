from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1


if __name__=="__main__":
    sol = Solution()
    s = "leetcode"
    print(sol.firstUniqChar(s))

# Time Complexity: O(n)
# Space Complexity: O(1)