def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = [0, 0]
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ans = [i, j]
    return ans
