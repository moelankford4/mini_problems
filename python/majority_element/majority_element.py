# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

import timeit

class majority_element(object):
    def compute(self, nums):
        majority = 0
        count = 0
        for i in range(len(nums)):
            if count == 0 and majority != nums[i]:
                majority = nums[i]
                count += 1
            elif nums[i] == majority:
                count += 1
            else: 
                count -= 1
        return majority

    
if __name__=="__main__":
    obj = majority_element()
    obj.compute([2,2,1,1,1,2,2])
    execution_time = timeit.timeit(lambda: obj.compute([2,2,1,1,1,2,2,5,3,2,1,3,4,7,6,5,4,3,2,2,4,6,7,77,7,6,5,4,3,3,54,5,6,6,4,5]), number=100)
    print(execution_time)

