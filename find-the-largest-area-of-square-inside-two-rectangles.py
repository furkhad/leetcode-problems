class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # Iterate through every unique pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                
                # Calculate the intersection coordinates
                # The start of the intersection is the max of the starts
                min_x = max(bottomLeft[i][0], bottomLeft[j][0])
                min_y = max(bottomLeft[i][1], bottomLeft[j][1])
                
                # The end of the intersection is the min of the ends
                max_x = min(topRight[i][0], topRight[j][0])
                max_y = min(topRight[i][1], topRight[j][1])
                
                # Check if the intersection is valid (width > 0 and height > 0)
                if min_x < max_x and min_y < max_y:
                    width = max_x - min_x
                    height = max_y - min_y
                    
                    # The largest square in a rectangle is determined by the shorter side
                    current_side = min(width, height)
                    
                    if current_side > max_side:
                        max_side = current_side
                        
        return max_side * max_side
