class Solution(object):
    def maxArea(self, height):
        lp = 0
        rp = len(height) - 1
        maxArea = 0 
        
        while (lp < rp):
            area = min(height[lp],height[rp])*(rp-lp)
            if area > maxArea:
                maxArea = area
            if(height[lp] <= height[rp]):
                lp += 1
            elif(height[rp] < height[lp]):
                rp -= 1
        return maxArea