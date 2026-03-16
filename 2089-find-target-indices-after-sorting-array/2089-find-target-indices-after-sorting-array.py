class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(nums)):
            if sorted(nums)[i]==target:
                output.append(i)
        return output