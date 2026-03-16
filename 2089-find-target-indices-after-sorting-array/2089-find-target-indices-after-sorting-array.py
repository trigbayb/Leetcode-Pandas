class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        couter_numbers_before_targets=0
        counter_targets=0
        for i in range(len(nums)):
            if nums[i]<target:
                couter_numbers_before_targets+=1
            elif nums[i]==target:
                counter_targets+=1
        return list(range(couter_numbers_before_targets, couter_numbers_before_targets+counter_targets))