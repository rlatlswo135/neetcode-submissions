class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # 높이가 오름차순이 되도록 인덱스 저장
        max_area = 0

        # 마지막에 0을 추가해서 스택을 전부 비우도록 함
        extended = heights + [0]

        for right, height in enumerate(extended):
            while stack and extended[stack[-1]] > height:
                mid = stack.pop()

                h = extended[mid]

                # pop 후 남은 인덱스가 왼쪽 경계
                left = stack[-1] if stack else -1

                width = right - left - 1
                max_area = max(max_area, h * width)

            stack.append(right)

        return max_area