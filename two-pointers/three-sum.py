# INSIGHT: sort the array and find the triplets without taking duplicates into account
# WHY IT WORKS: because sorting enables the criteria to increment or decrement a pointer and also to identify duplicates
# COMPLEXITY: time O(n^2) / space O(1)
# BREAKS WHEN: empty array or less than 3 elements — range loop doesn't execute, returns [] correctly
#              all same number non-zero e.g. [1,1,1] — i skip handles it, returns [] correctly
#              all zeros [0,0,0] — returns [[0,0,0]] correctly
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        unique_nums = sorted(nums)
        result =list()
        
        for i in range(len(unique_nums)):
            if (i==0) or (i!=0 and unique_nums[i] != unique_nums[i-1]):
                left = i + 1
                target = -1 * (unique_nums[i])
                right = len(unique_nums) - 1 
                while left < right:
                    if unique_nums[left] + unique_nums[right] == target:
                        result.append([unique_nums[i],unique_nums[left],unique_nums[right]])
                        while left < right and unique_nums[left] == unique_nums[left+1]:
                            left += 1
                        while left < right and unique_nums[right] == unique_nums[right-1]:
                            right -= 1
                        left +=1
                        right -=1
                    elif unique_nums[left] + unique_nums[right] > target:
                        right -=1
                    else:
                        left +=1
        return result
                



        