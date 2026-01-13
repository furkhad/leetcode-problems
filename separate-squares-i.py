from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        Calculates the minimum y-coordinate such that the area of squares above
        equals the area of squares below.
        
        Uses a Sweep-Line algorithm to process y-intervals.
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        total_area = 0
        events = []
        
        # Step 1: Create sweep-line events
        # We only care about y-coordinates and the side length (width)
        # squares[i] = [x, y, l]
        for _, y, l in squares:
            total_area += l * l
            events.append((y, l))       # Bottom edge adds width l
            events.append((y + l, -l))  # Top edge removes width l
            
        # Step 2: Sort events by y-coordinate
        events.sort(key=lambda x: x[0])
        
        target = total_area / 2.0
        current_area = 0.0
        current_width = 0
        
        # Step 3: Iterate through intervals
        for i in range(len(events) - 1):
            y, diff = events[i]
            current_width += diff
            
            next_y = events[i+1][0]
            
            # Only calculate area if we move up in y-coordinate
            if next_y > y:
                height = next_y - y
                chunk_area = current_width * height
                
                # Check if the split line is within this horizontal strip
                if current_area + chunk_area >= target:
                    missing_area = target - current_area
                    # Avoid division by zero, though logically strictly positive width is required to accumulate area
                    return y + missing_area / current_width
                
                current_area += chunk_area
                
        return float(events[-1][0])
