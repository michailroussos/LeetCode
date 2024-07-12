class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = list(s)  # Convert string to list for easy manipulation
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                start = stack.pop()
                end = i
                # Reverse the substring inside the current pair of parentheses
                s[start+1:end] = s[start+1:end][::-1]
        
        # Remove all parentheses from the string
        result = [c for c in s if c != '(' and c != ')']
        
        return ''.join(result)


# Create an instance of the Solution class
solution = Solution()

# Call the minOperations method with test input
#s ="(abcd)"
s="a(bcdefghijkl(mno)p)q"
result = solution.reverseParentheses(s)

print(f"The resulting string is : {result}")