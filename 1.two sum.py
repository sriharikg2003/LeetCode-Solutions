class Solution(object):
    def twoSum(self, nums, target):

        self.nums=nums
        self.target=target
        d=dict()
        for i in range(len(self.nums)):
            if (self.target-self.nums[i]) not in d.keys():
                d[self.nums[i]]=i
            else :
                return [i,d[self.target-self.nums[i]]]