class Solution(object):
    def fizzBuzz(self, n):
        # Constraint check
        if n < 1 or n > 10**4:
            return "Input n must be between 1 and 10^4"

        array = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                array.append("FizzBuzz")
            elif i % 3 == 0:
                array.append("Fizz")
            elif i % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(i))
        return array

if __name__ == "__main__":
    sol = Solution()
    n = 3
    result = sol.fizzBuzz(n)
    print(result)
