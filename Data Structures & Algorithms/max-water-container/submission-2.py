class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxim = 0
        while l<r: 
            vol = min(heights[l],heights[r]) * (r - l)
            if vol > maxim:
                maxim = vol
            
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else: 
                r-=1
    
        return maxim
            
