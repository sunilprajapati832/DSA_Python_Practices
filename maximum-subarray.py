class Solution:
    def maxSubArray(self, nums):
        def helper(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)
            cross_max = find_cross_max(left, mid, right)
            return max(left_max, right_max, cross_max)

        def find_cross_max(left, mid, right):
            left_sum = float('-inf')
            sum = 0
            for i in range(mid, left - 1, -1):
                sum += nums[i]
                left_sum = max(left_sum, sum)

            right_sum = float('-inf')
            sum = 0
            for i in range(mid + 1, right + 1):
                sum += nums[i]
                right_sum = max(right_sum, sum)

            return left_sum + right_sum

        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))

# Time Complexity: O(n log n)
# Space Complexity: O(log n) for recursion stack