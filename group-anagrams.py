class Solution(object):
    def groupAnagrams(self, strs):
        hash_map = {}

        for word in strs:
            # Sorted version of the word will be the key
            sorted_word = ''.join(sorted(word))

            if sorted_word not in hash_map:
                hash_map[sorted_word] = []
            hash_map[sorted_word].append(word)

        return list(hash_map.values())


if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))

# Time Complexity:	O(n × m log m)
# Space	Complexity: O(n × m)

