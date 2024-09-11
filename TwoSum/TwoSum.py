class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(nums.index(nums[i]))
                    result.append(nums.index(nums[j], nums.index(nums[i])))
                    return result
        return

print(Solution().twoSum([3, 3, 6, 23, 1, 4, 7], 6))
