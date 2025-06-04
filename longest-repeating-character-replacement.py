from collections import defaultdict

# Define the class first
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # Check if current window is valid
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

# Call the function below the class
sol = Solution()  # Create an instance of the class
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))  # Output should be 4
