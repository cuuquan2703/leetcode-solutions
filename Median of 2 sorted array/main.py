class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            a = nums1
            nums1 = nums2
            nums2 = a

        s_length = len(nums1) + len(nums2)
        s_median = s_length // 2

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = s_median - i - 2

            nums1_left = nums1[i] if i >= 0 else float("-inf")
            nums1_right = nums1[i + 1] if i + 1 < len(nums1) else float("inf")
            nums2_left = nums2[j] if j >= 0 else float("-inf")
            nums2_right = nums2[j + 1] if j + 1 < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if s_length % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
