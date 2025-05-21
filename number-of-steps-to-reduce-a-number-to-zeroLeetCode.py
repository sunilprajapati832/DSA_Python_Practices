class Solution(object):
    def numberOfSteps(self, num):
        # Constraint check: Ensure num is a non-negative integer
        if num < 0 or num > 10**6:
            return "Error: num must be between 0 and 10^6"

        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2  # Integer division
            else:
                num -= 1
            count += 1
        return count

# Main block to run the function
if __name__ == "__main__":
    sol = Solution()
    number = 14
    steps = sol.numberOfSteps(number)
    print(steps)
