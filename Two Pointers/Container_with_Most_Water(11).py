class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        mostWater = 0

        while left < right:
            h = min(height[left], height[right])
            l = right - left
            curr_water = l*h
            mostWater = max(mostWater, curr_water)

            if height[left] < height[right]:
                left  += 1
            
            else:
                right -= 1
            
        return mostWater