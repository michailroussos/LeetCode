class Solution:
    def minOperations(self, logs: list[str]) -> int:
        counter = 0
        for log in logs:
            if log == "../":
                counter = max(0, counter - 1)
            elif log == "./":
                continue
            else:
                counter += 1

        return counter 


# Create an instance of the Solution class
solution = Solution()

# Call the minOperations method with test input
logs =["d1/","d2/","../","d21/","./"]
operations = solution.minOperations(logs)

print(f"The number of operations needed is : {operations}")