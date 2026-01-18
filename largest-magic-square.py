class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. Precompute Prefix Sums for Rows and Columns
        # rows[i][j] stores sum of grid[i][0]...grid[i][j-1]
        # cols[i][j] stores sum of grid[0][j]...grid[i-1][j]
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]
        
        # 2. Iterate size k from largest possible down to 2
        for k in range(min(m, n), 1, -1):
            # Iterate through every possible top-left corner (r, c)
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    
                    # 3. Check Diagonals first (Manual summation)
                    d1 = 0 # Main diagonal
                    d2 = 0 # Anti-diagonal
                    for i in range(k):
                        d1 += grid[r + i][c + i]
                        d2 += grid[r + i][c + k - 1 - i]
                    
                    if d1 != d2:
                        continue # Diagonals don't match, move to next square
                    
                    target = d1
                    valid = True
                    
                    # 4. Check Rows (O(1) using prefix sums)
                    for i in range(r, r + k):
                        if row_prefix[i][c + k] - row_prefix[i][c] != target:
                            valid = False
                            break
                    if not valid: continue
                        
                    # 5. Check Columns (O(1) using prefix sums)
                    for j in range(c, c + k):
                        if col_prefix[r + k][j] - col_prefix[r][j] != target:
                            valid = False
                            break
                    
                    # If we pass all checks, this k is the answer
                    if valid:
                        return k
                        
        # If no square size >= 2 is found, the answer is 1
        return 1
