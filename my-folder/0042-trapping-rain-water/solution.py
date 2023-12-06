class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        # Fill left_max
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # Fill right_max
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate trapped water
        water_trapped = 0
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - height[i]

        return water_trapped

