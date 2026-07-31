class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                one += 1
                two += 1
            elif nums[i] == 1:
                one += 1
                two += 1
            else:
                two += 1
            print('index: ', i)
            print(zero, one, two)

        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i < one:
                nums[i] = 1
            else:
                nums[i] = 2
        