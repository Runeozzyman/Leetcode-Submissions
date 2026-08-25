class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)
        ans = []
        sorted_nums = sorted(nums)

        for fixed in range(n - 2):

            if fixed > 0 and sorted_nums[fixed] == sorted_nums[fixed - 1]:
                continue

            left = fixed + 1
            right = n - 1
            target = sorted_nums[fixed]

            while left < right:
                cur_sum = sorted_nums[left] + sorted_nums[right] + target

                if cur_sum == 0:
                    ans.append([target, sorted_nums[left], sorted_nums[right]])

                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

                elif cur_sum < 0:
                    left += 1

                else:
                    right -= 1

        return ans