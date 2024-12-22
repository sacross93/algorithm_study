"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

## 풀이과정
num1 = [1,3]
num2 = [2]

num = num1 + num2
num.sort()

len(num) / 2

num[len(num) // 2]


num1 = [1,2]
num2 = [3,4]

num = num1 + num2
num.sort()

len(num) / 2

num[len(num) / 2]

if len(num) % 2 != 0:
    median = [int(len(num) / 2 - 0.5)]
else:
    median = [int(len(num) / 2 - 1), int(len(num) / 2)]

if len(median) == 1:
    result = num[median[0]]
else:
    result = (num[median[0]] + num[median[1]]) / 2

print(result)
## 풀이 완료
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        if len(num) % 2 != 0:
            median = [int(len(num) / 2 - 0.5)]
        else:
            median = [int(len(num) / 2 - 1), int(len(num) / 2)]
        if len(median) == 1:
            result = num[median[0]]
        else:
            result = (num[median[0]] + num[median[1]]) / 2
        return result
