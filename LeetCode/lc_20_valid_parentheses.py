# Problem: Valid Parentheses
# Platform: LeetCode #20
# Topic: Stack + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s: str) -> bool:
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    return not stack

if __name__ == "__main__":
    print(isValid("()[]{}"))   # True
    print(isValid("([)]"))     # False
    print(isValid("{[]}"))     # True
