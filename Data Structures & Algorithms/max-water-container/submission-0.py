class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left_end = 0
        right_end = len(heights) - 1

        while left_end <= right_end:
            width = min(heights[left_end], heights[right_end])
            length = right_end - left_end

            if max_water < (width * length):
                max_water = width * length
            if heights[left_end] < heights[right_end]:
                left_end += 1
            else:
                right_end -= 1
        
        return max_water