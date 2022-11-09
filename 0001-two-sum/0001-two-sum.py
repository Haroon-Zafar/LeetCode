class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):

            differenceOfTwoNumbers = target - num

            if differenceOfTwoNumbers in dict:
                return [ dict[differenceOfTwoNumbers],index]

            else:
                dict[num] = index 
    