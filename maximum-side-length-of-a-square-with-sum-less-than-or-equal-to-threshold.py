class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        
        # 1. Build 2D Prefix Sum Array
        # P[i][j] stores the sum of the rectangle from (0,0) to (i-1, j-1)
        # We use size (rows + 1) x (cols + 1) to handle boundary checks easily (1-based indexing)
        P = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # Current cell + sum of top rect + sum of left rect - sum of overlap
                P[r][c] = mat[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]
        
        max_len = 0
        
        # 2. Iterate through every possible bottom-right corner (r, c)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # We attempt to find a square ONLY of size (max_len + 1).
                # If we find one, we increment max_len. If not, we continue.
                # This keeps the complexity linear O(MN) rather than O(MN * min(M,N)).
                current_side = max_len + 1
                
                if r >= current_side and c >= current_side:
                    # Calculate sum of square with side length 'current_side' ending at (r, c)
                    # Formula: Total - TopStrip - LeftStrip + Overlap
                    r1 = r - current_side
                    c1 = c - current_side
                    
                    total = P[r][c] - P[r1][c] - P[r][c1] + P[r1][c1]
                    
                    if total <= threshold:
                        max_len += 1
                        
        return max_len
