import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 핵심은 목적지에 가까운 차량부터 보면서 도착 시간을 비교하는 것입니다.
        # - 현재 차량의 시간이 last_time보다 크면 새로운 fleet
        # - 작거나 같으면 앞 fleet을 따라잡으므로 같은 fleet
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets