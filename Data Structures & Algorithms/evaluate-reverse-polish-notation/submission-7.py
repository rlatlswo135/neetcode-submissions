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
        # 숫자 넣다가 # + * - 만나먼 여태쌓인 녀석 연산
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