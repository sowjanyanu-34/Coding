# Container With Most Water (Leetcode 11)
from collections import Counter, defaultdict
from turtle import right
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
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                k += 1

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

#  Leetcode 11 Container With Most Water 
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

# Fruit Into Baskets leetcode 904
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

#  Maximum Average Subarray I leetcode 643
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

#leetcode 451 Sort Characters By Frequency
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        result=""
        for ch,countt in freq.most_common():
            result+=ch*countt
        return result        

#longest consecutive sequence (leetcode 128)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        long=0
        for n in numSet:
            if n-1 not in numSet:
                len=1
                while n+len in numSet:
                    len+=1
                long=max(long,len)
        return long


### Kadane's Algorithm
#leetcode 53 Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_s=nums[0]
        c_s=nums[0]
        for i in range(1,len(nums)):
            c_s=max(nums[i],c_s+nums[i])
            m_s=max(c_s,m_s)
        return m_s
    
#leetcode 152 Maximum product subarray
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p=1
        s=1
        ans=float('-inf')
        n=len(nums)
        for i in range(n):
            if p==0:
                p=1
            if s==0:
                s=1
            p*=nums[i]
            s*=nums[n-i-1]
            ans=max(ans,p,s)
        return ans
    
#Leetcode 1749 Maximum Absolute Sum of Any Subarray
class Solution: 
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        min_sum=0
        c_max=0
        c_min=0
        for n in nums:
            c_max=max(n,c_max+n)
            c_min=min(n,c_min+n)
            max_sum=max(max_sum,c_max)
            min_sum=min(min_sum,c_min)
        return max(max_sum,abs(min_sum))

#leetcode  918 Maximum Sum Circular Subarray
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        c_max=0
        c_min=0
        max_sum=nums[0]
        min_sum=nums[0]
        for num in nums:
            total+=num
            c_max=max(num,num+c_max)
            max_sum=max(max_sum,c_max)
            c_min=min(num,num+c_min)
            min_sum=min(min_sum,c_min)
        if total<0:
            return max_sum
        return max(max_sum,total-min_sum)
    
### Recursion
# 509 Fibonacci Number
class Solution: 
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
    
# 344 Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
      l,r=0,len(s)-1
      while l<r:
          s[l],s[r]=s[r],s[l]
          l+=1
          r-=1

##Prefix Sum
#724 Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_s=sum(nums)
        left_s=0
        for i in range(len(nums)):
            if left_s==total_s-left_s-nums[i]:
                return i
            left_s+=nums[i]
        return -1
    
# 1991 Find the middle index in array 
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_s=sum(nums)
        left_s=0
        for i in range(len(nums)):
            if left_s==total_s-left_s-nums[i]:
                return i
            left_s+=nums[i]
        return -1
    
# Product of Array Except Self (Leetcode 238)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        for i in range(len(nums)):
            ans[i]*=nums[i]
        r=1
        for i in range (n-1,-1,-1):
            ans[i]*=r
            r*=nums[i]
        return ans


# 523 Leetcode Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_s=0
        mpp={0:-1}
        for i in range(len(nums)):
            prefix_s+=nums[i]
            rem=prefix_s%k
            if rem in mpp:
                if i-mpp[rem]>1:
                    return True
            else:
                mpp[rem]=i
        return False      
          
#26 Remove Duplicates from Sorted Array
class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k

# leetcode 27 Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
           if nums[i]!=val:
               nums[k]=nums[i]
               k+=1
        return k 

# 977 Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        h=0
        t=n-1
        for pos in range(n-1,-1,-1):
            if abs(nums[h])>abs(nums[t]):
                res[pos]=nums[h]*nums[h]
                h+=1
            else:
                res[pos]=nums[t]*nums[t]
                t-=1
        return res

# 881 Boats to Save People
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        boat=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            else:
                r-=1
            boat+=1
        return boat
    
#Trapping Rain Water leetcode (42)
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=height[left]
        right_max=height[right]
        water=0
        while left<right:
            if left_max<right_max:
                left+=1
                left_max=max(left_max,height[left])
                water+=left_max-height[left]
            else:
                right-=1
                right_max=max(right_max,height[right])
                water+=right_max-height[right]
        return water

# Running Sum of 1d Array leetcode 1480
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
 
 # Range Sum Query - Immutable 303 leetcode
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix=[0]
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]

#leetcode 560 Subarray sum equals k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        count=0
        prefix_map={0:1}
        for num in nums:
            curr_sum+=num
            if (curr_sum-k) in prefix_map:
                count+=prefix_map[curr_sum-k]
            prefix_map[curr_sum]=prefix_map.get(curr_sum,0)+1
        return count

