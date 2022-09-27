class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, low, high, target):  
            if high >= low:
                mid = (low+high)//2

                if nums[mid] == target:
                    #result = mid
                    return mid
                elif nums[mid] > target >= nums[low]:
                    return binarySearch(nums, low, mid-1, target)
                elif nums[mid] < target <= nums[high]:
                    return binarySearch(nums, mid+1, high, target)
                elif nums[mid] > nums[high]:
                    return binarySearch(nums, mid+1, high, target)
                #elif nums[mid] < nums[low]:
                else:
                    return binarySearch(nums, low, mid-1, target)
            else: return -1
                
        
        return binarySearch(nums, 0, len(nums)-1, target)