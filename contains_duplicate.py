class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen= set()
        for j in nums:
            if j in seen:
                return True
            seen.add(j)
        return False