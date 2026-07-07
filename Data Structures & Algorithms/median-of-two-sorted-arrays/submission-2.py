class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 1:
            # odd number of elements
            middle = len(nums1) // 2
            median = nums1[middle]
        else:
            # even number of elements
            middle = len(nums1) // 2
            median = (nums1[middle - 1] + nums1[middle]) / 2
        return median