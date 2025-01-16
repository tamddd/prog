class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solver(l, now, idx):
            if target < now:
                return
            elif target == now:
                #copyしている
                ans.append(l[::])
            else:
                #今見ているidxを使う
                l.append(candidates[idx])
                solver(l, now+candidates[idx], idx)
                l.pop()
                #使わない
                if idx+1 < len(candidates):
                    solver(l, now, idx+1)
        solver([], 0, 0)
        return ans
