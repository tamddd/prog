class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solver(used_index, nl):
            if len(used_index) == len(nums):
                res.append(nl[::])
            else:
                for i in range(len(nums)):
                    if i in used_index:
                        continue
                    else:
                        used_index.add(i)
                        nl.append(nums[i])
                        solver(used_index, nl)
                        used_index.discard(i)
                        nl.pop()
        solver(set(), [])
        return res
