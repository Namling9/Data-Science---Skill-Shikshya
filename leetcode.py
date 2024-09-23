# # Q.1 
# class Solution(object):
#     def uncommonFromSentences(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: List[str]
#         """
#         sen1 = list(s1.split(" "))
#         sen2 = list(s2.split(" "))
#         sen3 = sen1+sen2
        
#         return [i for i in sen3 if sen3.count(i) <= 1]
    
# s1 = "this apple is sweet"
# s2 = "this apple is sour"

# ans = Solution()
# print(ans.uncommonFromSentences(s1,s2))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [2,7,11,15]
target = 9

ans = Solution()
print(ans.twoSum(nums,target))