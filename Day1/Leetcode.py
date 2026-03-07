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
                
# Sort Colors (Leetcode 75)
class Solution:    
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Container With Most Water (Leetcode 11)
class Solution:
    def maxArea(self,height:List[int])->int:
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            width=r-l
            h=min(height[l],height[r])
            area=h*width
            max_area=max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
    
#Valid Palindrome (Leetcode 125):
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter=[]
        for ch in s:
            if ch.isalnum():
                filter.append(ch.lower())
        l=0
        r=len(filter)-1
        while l<r:
            if filter[l]!=filter[r]:
                return False
            l+=1
            r-=1
        return True
    
# leetcode 1423 Maximum Points You Can Obtain from Cards:
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        lsum=0
        rsum=0
        maxsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum=lsum
        rindex=n-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            rindex-=1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum

#leetcode 904 Fruit Into Baskets
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        l=0
        max_fruits=0
        for r in range(len(fruits)):
            count[fruits[r]]=count.get(fruits[r],0)+1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            max_fruits=max(max_fruits,r-l+1)
        return max_fruits

# 643 Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=0
        for i in range(k):
            w+=nums[i]
        max_s=w
        for i in range(k,len(nums)):
           w+=nums[i]
           w-=nums[i-k]
           if w>max_s:
            max_s=w
        return max_s/k
    
#485 Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        count=0
        for n in nums:
            if n==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
        return max_count

#713 Subarray less than k
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l=0
        c=0
        p=1
        for r in range(len(nums)):
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            c+=r-l+1
        return c

#leetcode 169 majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ele=0
        for i in nums:
            if count==0:
                ele=i
                count=1
            elif i==ele:
                count+=1
            else:
                count-=1
        return ele