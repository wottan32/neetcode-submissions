class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lista = []
        lista = set(nums)
        return len(lista) < len(nums)