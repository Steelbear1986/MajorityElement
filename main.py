class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=Counter(nums)
        return  ( [k  for k, v  in nums.items() if v==max(nums.values())][0])