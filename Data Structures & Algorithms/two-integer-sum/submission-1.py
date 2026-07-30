class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 🔑 INSTANTIATE the class first
solver = Solution()

# 🔑 CALL the method ON the instance
f = [3, 4, 5, 6]
target = 7
p = solver.twoSum(f, target)
print(p)  # Output: [0, 1]