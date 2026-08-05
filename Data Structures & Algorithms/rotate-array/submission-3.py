class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def roatate_one(lst):
            prev = lst[0]
            for i in range(0, len(lst)):
                nex_i = (i + 1) % len(lst)
                temp = prev
                prev = lst[nex_i]
                lst[nex_i] = temp
        for _ in range(k):
            roatate_one(nums)

        
            

        