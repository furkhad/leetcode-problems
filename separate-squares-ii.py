from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Step 1: Coordinate Compression for X-axis
        # We need to map the large x-coordinates to small indices for the Segment Tree.
        xs = set()
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
        
        # Sort distinct x coordinates to create elementary intervals
        unique_x = sorted(list(xs))
        x_map = {x: i for i, x in enumerate(unique_x)}
        m = len(unique_x)
        
        # Step 2: Segment Tree Setup
        # 'count': tracks how many active squares cover a specific interval range
        # 'length': tracks the actual physical length of the union of active intervals
        tree_count = [0] * (4 * m)
        tree_length = [0.0] * (4 * m)

        def update(node, start, end, l, r, val):
            """
            node: current tree index
            start, end: range of indices in unique_x covered by this node (start inclusive, end exclusive)
            l, r: range of indices we want to update (l inclusive, r exclusive)
            val: +1 for adding a square, -1 for removing
            """
            if l >= end or r <= start:
                return

            if l <= start and end <= r:
                tree_count[node] += val
            else:
                mid = (start + end) // 2
                update(2 * node, start, mid, l, r, val)
                update(2 * node + 1, mid, end, l, r, val)
            
            # Recalculate the active length for this node
            if tree_count[node] > 0:
                # If this node is covered by at least one square, its length is the full width of the interval
                tree_length[node] = unique_x[end] - unique_x[start]
            else:
                # If count is 0, the length is the sum of its children (unless it's a leaf)
                if end - start == 1:
                    tree_length[node] = 0.0
                else:
                    tree_length[node] = tree_length[2 * node] + tree_length[2 * node + 1]

        # Step 3: Create and Sort Events
        # Events: (y, type, x_start_idx, x_end_idx)
        # Type 1 = bottom edge (enter), -1 = top edge (exit)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x_map[x], x_map[x + l]))
            events.append((y + l, -1, x_map[x], x_map[x + l]))
        
        events.sort() # Sort by y-coordinate

        # Step 4: Sweep-Line Process
        total_area = 0.0
        strips = [] # To store (y_start, y_end, active_width, area_chunk)
        
        prev_y = events[0][0]
        i = 0
        n_events = len(events)
        
        # The root of the segment tree covers the range [0, m-1)
        root_range = m - 1
        
        while i < n_events:
            curr_y = events[i][0]
            
            # Calculate area accumulated in the vertical strip since the last event
            h = curr_y - prev_y
            active_width = tree_length[1] # Root is at index 1
            
            if h > 0 and active_width > 0:
                area_chunk = active_width * h
                total_area += area_chunk
                strips.append((prev_y, curr_y, active_width, area_chunk))
            
            # Process all events happening at this exact y-coordinate
            while i < n_events and events[i][0] == curr_y:
                _, type_, x1, x2 = events[i]
                update(1, 0, root_range, x1, x2, type_)
                i += 1
            
            prev_y = curr_y
            
        # Step 5: Find the exact split line
        target = total_area / 2.0
        current_area = 0.0
        
        for y_start, y_end, width, area_chunk in strips:
            if current_area + area_chunk >= target:
                # The answer is inside this strip.
                # We need 'needed' more area from this strip.
                # needed = width * (y_ans - y_start)
                needed = target - current_area
                return y_start + (needed / width)
            current_area += area_chunk
            
        return float(prev_y)
