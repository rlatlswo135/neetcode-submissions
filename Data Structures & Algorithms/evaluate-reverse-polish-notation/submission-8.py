def operation(num1,num2,operator):
    match operator:
        case "+":
            return int(num1) + int(num2)
        case "-":
            return int(num1) - int(num2)
        case "*":
            return int(num1) * int(num2)
        case "/":
            return int(int(num1) / int(num2))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}

        nums = []

        for token in tokens:
            if token in operators:
                num2 = nums.pop()
                num1 = nums.pop()
                result = operation(num1,num2,token)
                nums.append(result)
            else:
                nums.append(token)

        return int(nums[0])