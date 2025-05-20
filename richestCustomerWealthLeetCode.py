class Solution(object):
    def maximumWealth(self, accounts):
        # Helper function to calculate sum of each sublist
        def sum_sublists(accounts):
            return [sum(sublist) for sublist in accounts]
        sums = sum_sublists(accounts)
        max1 = max(sums)
        return max1

# Main driver code
if __name__ == "__main__":
    # Input data
    accounts = [[1, 2, 3], [3, 2, 1]]

    # Create object of Solution class
    sol = Solution()

    # Call the function and print result
    result = sol.maximumWealth(accounts)
    print("Richest customer's wealth:", result)
