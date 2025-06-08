class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            # Shrink from left as long as total is valid
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

# time complexity = O(n)
# space complexity = O(1)

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
