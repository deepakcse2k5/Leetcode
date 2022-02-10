# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
from typing import List


class Solution:
    def maxDistanceToClosestPerson(self, seats: List[int]) -> int:
        prev_seat = None
        dist = float("-inf")
        for index in range(len(seats)):
            if seats[index]==1:
                if prev_seat == None:
                    dist = index
                else:
                    dist = max(dist, (index - prev_seat) // 2)
                prev_seat = index
        dist = max(dist, len(seats) - 1 - prev_seat)
        return dist


if __name__ == "__main__":
    sol = Solution()
    seats = [1, 0, 0, 0, 1, 0, 1]
    print(sol.maxDistanceToClosestPerson(seats))
