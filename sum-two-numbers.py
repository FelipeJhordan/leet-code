"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputList: List[int] = []
        isCorrectlyNumToSum = False
        for numIndex,num in enumerate(nums):
          
            cloneList: List[int] = nums[:]

            for numxIndex,numx in enumerate(cloneList):
                isSameIndex = numIndex  == numxIndex
                if not isSameIndex  and (numx + num) == target:
                    print(numIndex, numxIndex)
                    outputList = [numIndex, numxIndex]
                    isCorrectlyNumToSum = True
                    break
            if(isCorrectlyNumToSum):
                break
        return outputList 
       
        