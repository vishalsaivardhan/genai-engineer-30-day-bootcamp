# day-05

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique_numbers = set(nums)
        if len(nums) == len(unique_numbers):
            return False
        else:
            return True