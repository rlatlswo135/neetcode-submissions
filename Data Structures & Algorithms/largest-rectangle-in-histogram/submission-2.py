from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0  # 지금까지 찾은 가장 큰 직사각형의 넓이
        stack = []    # (시작 인덱스, 높이) 쌍을 저장하는 스택

        # 막대를 왼쪽부터 하나씩 확인한다
        for i, height in enumerate(heights):
            start = i  # 현재 높이의 직사각형은 일단 현재 막대부터 시작한다고 본다

            # 현재 막대보다 높은 후보는 현재 막대에서 오른쪽으로 더 뻗을 수 없다
            while stack and stack[-1][1] > height:
                start_index, previous_height = stack.pop()  # 경계에 막혀 끝난 후보를 꺼낸다

                # 현재 인덱스 i는 직사각형에 포함되지 않는 오른쪽 경계이므로 폭은 i - 시작 인덱스다
                width = i - start_index

                # 꺼낸 높이로 만들 수 있었던 직사각형의 넓이를 계산해 최댓값을 갱신한다
                max_area = max(max_area, previous_height * width)

                # 현재 높이는 방금 꺼낸 후보가 시작했던 위치까지 왼쪽으로 뻗을 수 있다
                start = start_index

            # 현재 높이 후보를 저장한다
            # 앞에서 꺼낸 막대가 있다면, 그 시작 위치를 이어받아 더 왼쪽부터 시작한다
            stack.append((start, height))

        # 배열 끝까지 낮은 막대를 만나지 못한 후보들은 배열 끝까지 뻗을 수 있다
        for start_index, height in stack:
            width = len(heights) - start_index  # 배열의 끝 인덱스는 len(heights)이므로 폭은 길이 - 시작 인덱스다

            # 남은 후보의 넓이를 계산해 최댓값을 갱신한다
            max_area = max(max_area, height * width)

        # 모든 후보의 넓이를 확인한 뒤 가장 큰 넓이를 반환한다
        return max_area