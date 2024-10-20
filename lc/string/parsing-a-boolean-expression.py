class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        # stack
        # time O(n), space O(n)
        stack = []
        
        for ch in exp:
            if ch == ',':
                continue
            elif ch in ['t', 'f', '!', '&', '|', '(']:
                # Push true/false, operators, or opening parentheses onto the stack
                stack.append(ch)
            elif ch == ')':
                # Evaluate the sub-expression when encountering a closing parenthesis
                operands = []
                
                # Pop elements until we find the corresponding opening parenthesis
                while stack and stack[-1] != '(':
                    operands.append(stack.pop())
                stack.pop()  # Pop the '('
                
                # Get the operator before '('
                operator = stack.pop()
                
                # Evaluate the result based on the operator
                if operator == '&':
                    # AND: True only if all operands are True
                    result = all(x == 't' for x in operands)
                elif operator == '|':
                    # OR: True if at least one operand is True
                    result = any(x == 't' for x in operands)
                elif operator == '!':
                    # NOT: Flip the single operand (t -> f or f -> t)
                    result = operands[0] == 'f'
                
                # Push the result back onto the stack as 't' or 'f'
                stack.append('t' if result else 'f')

        # The final result is the only element left in the stack
        return stack.pop() == 't'

# class Solution:
#     def dfs(self, exp):
#         if exp == "f": return False
#         if exp == "t": return True
#         arr = []
#         op = exp[0]
#         exp = exp[2:-1]
#         group = ""
#         bal = 0
#         for i in range(len(exp)):
#             group += exp[i]
#             if exp[i] == "(": bal += 1
#             elif exp[i] == ")": bal -= 1
#             if exp[i] == "," and bal == 0:
#                 arr.append(group[:-1])
#                 group = ""
#             elif exp[i] == "," and len(group) == 2:
#                 arr.append(group[0])
#                 group = ""

#         arr.append(group)        
#         cur = self.dfs(arr[0])
#         for i in range(1, len(arr)):
#             if op == "&":
#                 cur = cur and self.dfs(arr[i])
#             elif op == "|":
#                 cur = cur or self.dfs(arr[i])
#             else:
#                 cur = not cur
#         return cur if op != "!" else not cur
            
#     def parseBoolExpr(self, exp: str) -> bool:
#         # string & recursion
#         # time O(n^2), space O(n)
#         return self.dfs(exp)