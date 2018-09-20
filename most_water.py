# My solution has not been accepted yet but I'm fairly happy with this quick solution for now
# TODO: improve algorithm by making less computations
class Solution:
    # Not Pythonic naming convention but the way LeetCode wants
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0

        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area

        return max_area


height = [1,8,6,2,5,4,8,3,7]
print(Solution.maxArea(Solution(), height))
