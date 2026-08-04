class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pop_idx = stack.pop()
                result[pop_idx] = idx - pop_idx

            stack.append(idx)
        
        return result

