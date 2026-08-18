class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        values = {}
        for i in range(len(nums)):
            if nums[i] in values:
                if abs(i - values[nums[i]])<=k:
                   return True
            values[nums[i]] = i
        return False




        

            
        