def isValidOptimized(s:str)->bool:
    stack=[]; mapping={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in mapping.values(): stack.append(ch)
        elif ch in mapping.keys():
            if stack and stack[-1]==mapping[ch]: stack.pop()
            else: return False
    return not stack

if __name__=="__main__":
    print(isValidOptimized("()[]{}")) # True
    print(isValidOptimized("(]"))     # False

