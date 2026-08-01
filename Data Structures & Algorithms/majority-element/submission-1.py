class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # target threshold
        target = len(nums) // 2

        # some sort of data structure, set, list, dict, etc.?
        count = {}

        # for loop to loop through nums of size n
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

            if count[nums[i]] > target:
                return nums[i]
