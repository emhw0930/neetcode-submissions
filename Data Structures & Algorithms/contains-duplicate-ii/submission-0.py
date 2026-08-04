class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # make a map {val: index (last appear)}
        # for num in nums:
        #   if num in map: find the difference, 
        #       if the difference <= k reutrn True, 
        #       otherwise update the last appearance
        mapi = {}
        for i, num in enumerate(nums):
            if num in mapi:
                if i - mapi[num] <= k:
                    return True
                else:
                    mapi[num] = i
            else:
                mapi[num] = i
        return False
        
        