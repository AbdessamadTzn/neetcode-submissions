class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        my_stack = []
        n = len(heights)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while my_stack and height < my_stack[-1][0]:
                h, j = my_stack.pop()
                w = i-j
                a = w*h
                max_area = max(max_area, a)
                start = j
            my_stack.append((height, start))

        while my_stack:
            h, j = my_stack.pop()
            w = n-j
            max_area = max(max_area, h*w)
        
        return max_area
        