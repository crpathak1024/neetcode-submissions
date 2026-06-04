class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:  # Use <= to ensure we check all values
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1  # Move the right pointer left
            else:
                l = mid + 1  # Move the left pointer right
                
        return -1  # If target is not found



        