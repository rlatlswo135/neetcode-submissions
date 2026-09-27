class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            # 높이는 결국 현재 x가 존재하는 범위내에서 가장 작은게 될거
            # 그래야 겹치는 높이를 신경쓸 필요가 없으니까
            height = min(heights[left], heights[right])
            # 단순 비교위해 넣어주고
            max_area = max(max_area, width * height)
            # 만약 높이가 left가 더 낮다면 right는 이미 높다는거니까
            # left에서 right높이에 가까운걸 찾아야함
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area