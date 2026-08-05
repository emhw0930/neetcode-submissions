class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        result = []
        for num in nums1:
            set1.add(num)
        for num in nums2:
            if num in set1:
                set1.remove(num)
                result.append(num)
        return result