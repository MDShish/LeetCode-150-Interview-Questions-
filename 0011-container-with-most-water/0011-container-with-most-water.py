class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxArea = 0
        while(l<r):
            if(maxArea<min(heights[l],heights[r])*(r-l)):
                maxArea = min(heights[l],heights[r])*(r-l)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return maxArea



class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1

        maxArea = 0

        while l < r:

            area = (r - l) * min(height[l], height[r])

            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna