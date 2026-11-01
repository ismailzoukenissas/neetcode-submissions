from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # On compare chaque élément i avec les éléments j
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # On commence à i + 1 pour éviter l'auto-comparaison
                if nums[i] == nums[j]:
                    return True
        
        return False