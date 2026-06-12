import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
                        "+": operator.add,
                        "-": operator.sub,
                        "*": operator.mul,
                        "/": operator.truediv
                    }
        for i in tokens:
            if i in operations:
                right = stack.pop()
                left = stack.pop()

                result = operations[i](left, right)
                stack.append(int(result))
            else:
                stack.append(int(i))

        return stack[-1]