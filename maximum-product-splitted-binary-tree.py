class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def tree_sum(node):
            if not node:
                return 0
            curr_sum = node.val + tree_sum(node.left) + tree_sum(node.right)
            all_sums.append(curr_sum)
            return curr_sum

        total_sum = tree_sum(root)
        max_p = 0

        for s in all_sums:
            max_p = max(max_p, s * (total_sum - s))

        return max_p % (10**9 + 7)
