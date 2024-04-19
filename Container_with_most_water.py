class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            curr_area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, curr_area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left+=1
                right-=1
        return max_area
