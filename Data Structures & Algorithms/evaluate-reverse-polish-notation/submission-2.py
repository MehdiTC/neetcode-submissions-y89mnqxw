class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        set = {"+", "-", "*", "/"}

        a = int(tokens[0])
        i = 1
        for val in tokens:            
            if val == "+":
                b = stack.pop()
                a = stack.pop()
                res = a + b 
                stack.append(res)
            elif val == "-":
                b = stack.pop()
                a = stack.pop()
                res = a - b 
                stack.append(res)
            elif val == "*":
                b = stack.pop()
                a = stack.pop()
                res = a * b 
                stack.append(res)
            elif val == "/":
                b = stack.pop()
                a = stack.pop()
                res = int(a / b)
                stack.append(res) 
            else:
                stack.append(int(val))
            
        
        return stack[-1]



        