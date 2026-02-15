# Container With Most Water (Leetcode 11)
from collections import Counter, defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            group[key].append(s)
        return list(group.value())
    
#Valid anagram (Leetcode 242)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
#Two Sum (Leetcode 1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

#Two Sum II - Input Array Is Sorted (Leetcode 167)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            curr_sum=numbers[l]+numbers[r]
            if curr_sum==target:
                return [l+1,r+1]
            elif curr_sum<target:
                l+=1
            else:
                r-=1