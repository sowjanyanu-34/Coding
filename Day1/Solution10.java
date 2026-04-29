//Leetcode Hashing Pattern(Easy,Medium)
//Two Sum Problem (Leetcode 1)

package Daily_Coding.Day1;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        return new int[] {};
    }
}

// Conatins duplicate (Leetcode 217)
class Solution1 {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}

// Valid anagram(leetcode 242)
class Solution2 {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) {
            if (c != 0)
                return false;

        }
        return true;
    }
}

// Find unique characters in a string (Leetcode 387)
class Solution3 {
    public int firstUniqChar(String s) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}

// Subarray Sum Equals K (Leetcode 560)
class Solution4 {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int count = 0;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}

// Longest Consecutive Sequence leetcode 128
class Solution5 {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int longest = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int count = num;
                int current = 1;
                while (set.contains(current + 1)) {
                    current++;
                    count++;
                }
                longest = Math.max(longest, count);
            }
        }
        return longest;
    }
}

// Longest substring without repeating characters (Leetcode 3)
class Solution6 {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int left = 0;
        int max_longest = 0;
        for (int right = 0; right < s.length(); right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            max_longest = Math.max(max_longest, right - left + 1);
        }
        return max_longest;
    }
}

// Find all anagrams in a string (leetcode 438)
class Solution7 {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length())
            return result;
        int[] pCount = new int[26];
        int[] sCount = new int[26];
        for (char c : p.toCharArray()) {
            pCount[c - 'a']++;
        }
        int window = p.length();
        for (int i = 0; i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
            if (i >= window) {
                sCount[s.charAt(i - window) - 'a']--;
            }
            if (Arrays.equals(pCount, sCount)) {
                result.add(i - window + 1);
            }
        }
        return result;
    }
}

// Binary Search Pattern
// Binary Search (Leetcode 704)
class Solution8 {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

}

// Search Insert Position (Leetcode 35)
class Solution9 {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid + 1;
            }
        }
        return left;
    }
}

// leetcode 278

class VersionControl {
    boolean isBadVersion(int version) {
        int bad = 4; // suppose 4 is first bad version
        return version >= bad;
    }
}

public class Solution10 extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        Solution10 obj = new Solution10();
        System.out.println(obj.firstBadVersion(10));
    }
}

// Sqrt(x) (Leetcode 69)
class Solution11 {
    public int mySqrt(int x) {
        int left = 0;
        int right = x;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if ((long) mid * mid <= x) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
}

// leetcode 33
class Solution12 {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Left half sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Right half sorted
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}

// (leetcode 153)
class Solution13 {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return nums[l];
    }
}

// Find Peak Element (Leetcode 162)
class Solution14 {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[mid + 1]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}

// LEETCODE 189 Rotate Array
class Solution15 {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}

// 34 Find First and Last Position of Element in Sorted Array
class Solution16 {
    public int[] searchRange(int[] nums, int target) {
        int first = firstOccur(nums, target);
        if (first == -1)
            return new int[] { -1, -1 };
        int last = lastOccur(nums, target);
        return new int[] { first, last };
    }

    private int firstOccur(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int ans = -1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) {
                ans = m;
                r = m - 1;
            }
            if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return ans;
    }

    private int lastOccur(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int ans = -1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) {
                ans = m;
                l = m + 1;
            }
            if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return ans;
    }

}

// 875 koko Eating Bananas
class Solution17 {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;
        for (int pile : piles) {
            right = Math.max(right, pile);
        }

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canEat(piles, h, mid)) {

                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean canEat(int[] piles, int h, int k) {
        long hours = 0;
        for (int pile : piles) {
            hours += (pile + k - 1) / k;
        }
        return hours <= h;
    }
}

// 1011 Capacity To Ship Packages Within D Days
class Solution18 {
    public int shipWithinDays(int[] weights, int days) {
        int l = 0;
        int r = 0;
        for (int w : weights) {
            l = Math.max(l, w);
            r += w;
        }
        while (l < r) {
            int m = l + (r - l) / 2;
            if (canShip(weights, days, m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    private boolean canShip(int[] weights, int days, int cap) {
        int dayCount = 1;
        int currLoad = 0;
        for (int w : weights) {
            if (currLoad + w > cap) {
                dayCount++;
                currLoad = 0;
            }
            currLoad += w;
        }
        return dayCount <= days;
    }
}

// 1870 Minimum Speed to Arrive on Time
class Solution19 {
    public int minSpeedOnTime(int[] dist, double hour) {
        int n = dist.length;
        if (n - 1 > hour)
            return -1;
        int l = 1;
        int r = 10000000;
        int ans = -1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (canReach(dist, hour, m)) {
                ans = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return ans;
    }

    private boolean canReach(int[] dist, double hour, int speed) {
        double time = 0.0;
        for (int i = 0; i < dist.length; i++) {
            double t = (double) dist[i] / speed;
            if (i != dist.length - 1)
                time += Math.ceil(t);
            else
                time += t;
        }
        return time <= hour;
    }
}

// gfg Aggressive cows
class Solution20 {
    public int aggressiveCows(int[] stalls, int cows) {
        Arrays.sort(stalls);
        int l = 1;
        int r = stalls[stalls.length - 1] - stalls[0];
        int answer = 0;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (canPlace(stalls, cows, m)) {
                answer = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return answer;
    }

    private boolean canPlace(int[] stalls, int cows, int dist) {
        int count = 1;
        int last = stalls[0];
        for (int i = 1; i < stalls.length; i++) {
            if (stalls[i] - last >= dist) {
                count++;
                last = stalls[i];
            }
        }
        return cows >= count;
    }
}

// 1552 leetcode Magnetic Force Between Two Balls
class Solution21 {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int l = 1;
        int r = position[position.length - 1] - position[0];
        int ans = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (canPlace(position, m, mid)) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }

    private boolean canPlace(int[] position, int m, int dist) {
        int count = 1;
        int last = position[0];
        for (int i = 1; i < position.length; i++) {
            if (position[i] - last >= dist) {
                count++;
                last = position[i];
            }
        }
        return count >= m;
    }
}

// leetcode 1482 Minimum Number of Days to Make m Bouquets
class Solution22 {
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long) m * k > bloomDay.length)
            return -1;
        int l = Integer.MAX_VALUE;
        int r = Integer.MIN_VALUE;
        for (int d : bloomDay) {
            l = Math.min(l, d);
            r = Math.max(r, d);
        }
        int ans = -1;
        while (l <= r) {
            int min = l + (r - l) / 2;
            if (canR(bloomDay, m, k, min)) {
                ans = min;
                r = min - 1;
            } else {
                l = min + 1;
            }
        }
        return ans;
    }

    private boolean canR(int[] bloomDay, int m, int k, int day) {
        int count = 0;
        int bbb = 0;
        for (int d : bloomDay) {
            if (d <= day) {
                count++;
                if (count == k) {
                    bbb++;
                    count = 0;
                }
            } else {
                count = 0;
            }
        }
        return bbb >= m;
    }
}

// gfg Allocate minimum number of pages
class Solution23 {
    public int findPages(int[] arr, int k) {
        int n = arr.length;
        if (k > n)
            return -1;
        int l = 0;
        int r = 0;
        for (int pages : arr) {
            l = Math.max(l, pages);
            r += pages;
        }
        int ans = -1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (canAllocate(arr, k, m)) {
                ans = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return ans;
    }

    private static boolean canAllocate(int[] arr, int k, int maxpages) {
        int student = 1;
        int pagesum = 0;
        for (int pages : arr) {
            if (pagesum + pages <= maxpages) {
                pagesum += pages;
            } else {
                student++;
                pagesum = pages;
            }
        }
        return student <= k;
    }

    public void main(String[] args) {
        int arr[] = { 10, 20, 30, 40 };
        int k = 2;
        System.out.println(findPages(arr, k));
    }
}

// 74 leetcode Search in 2D matrix
class Solution24 {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;
        int m = matrix.length;
        int n = matrix[0].length;
        int l = 0;
        int r = m * n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int row = mid / n;
            int col = mid % n;
            int value = matrix[row][col];
            if (value == target) {
                return true;
            } else if (value < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return false;
    }
}