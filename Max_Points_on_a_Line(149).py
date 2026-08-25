class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n<3:
            return n
        
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            dx = x2-x1
            if dx == 0:
                return float('inf')
            return (y2-y1)/dx
        
        ans = 1

        for i, p1 in enumerate(points):

            slopes = defaultdict(int)

            for j, p2 in enumerate(points[i+1:]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)

        return ans+1