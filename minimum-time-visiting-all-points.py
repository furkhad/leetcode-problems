from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        LeetCode 1266. Minimum Time Visiting All Points
        
        Calculates the minimum time to visit all points in the given order.
        Moving vertically, horizontally, or diagonally takes 1 second.
        This is equivalent to the Chebyshev distance between adjacent points.
        """
        total_time = 0
        
        # Iterate through the points from the first to the second-to-last
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            next_x, next_y = points[i+1]
            
            # The time to travel between two points is the maximum of the absolute 
            # difference in their x or y coordinates (Chebyshev distance).
            delta_x = abs(next_x - curr_x)
            delta_y = abs(next_y - curr_y)
            
            total_time += max(delta_x, delta_y)
            
        return total_time
