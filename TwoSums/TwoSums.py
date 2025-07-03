class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        
        
        # another solution using dictionary
        """
        # Dictionary to store numbers and their corresponding indices
        num_map = {}
        
        # Loop through each number in the array
        for i, num in enumerate(nums):
            complement = target - num
            # If the complement is in the dictionary, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_map[num] = i
        
        # If no solution found, return an empty list
        return []
        """