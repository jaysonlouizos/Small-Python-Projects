
def bracket_check(x:str) -> bool:
    stack = []
    
    for char in x:
        print(stack)
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) > 0:
        return False
    return True