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

# Move Zeros (leetcode 283)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insertPos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != insertPos:
                    nums[i], nums[insertPos] = nums[insertPos], nums[i]
                insertPos += 1

# leetcode 680 Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
                
