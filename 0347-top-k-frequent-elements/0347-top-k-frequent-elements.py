class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i],0)+1
        arr = sorted(frequency, key=frequency.get, reverse=True)
        return arr[:k]
        