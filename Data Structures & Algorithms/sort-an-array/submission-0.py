class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # base case: if array is size 1 or 0, already sorted and stop splitting
        if len(nums) <= 1:
            return nums

        # splitting algorithm
        mid = len(nums) // 2      # // ensures we get a clean integer for the index
        left_half = nums[:mid]    # Grabs everything from the start up to the 'mid' index
        right_half = nums[mid:]   # Grabs everything from the 'mid' index to the end

        # recursion
        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        # merge logic
        sorted_result = []

        i = 0
        j = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sorted_result.append(left_half[i])
                i += 1
            else:
                sorted_result.append(right_half[j])
                j += 1

        # Sweep up any remaining elements
        sorted_result.extend(left_half[i:])
        sorted_result.extend(right_half[j:])

        return sorted_result