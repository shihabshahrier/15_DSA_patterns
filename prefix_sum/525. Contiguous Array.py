class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        mx = 0
        dic = {}
        for i, v in enumerate(nums):
            s += 1 if v == 1 else -1
            if s == 0:
                mx = i + 1
            elif s in dic:
                mx = max(mx, i - dic[s])
            else:
                dic[s] = i
        return mx
            