class Solution:
    def is_overlapped(self, pre_end, cur_start):
        return cur_start <= pre_end

    def merge(self, pre_end, cur_start):
        return max(pre_end, cur_start)

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ret = [intervals[0]]
        for s, e in intervals[1:]:
            # 被るならまとめる
            if self.is_overlapped(ret[-1][1], s):
                ret[-1][1] = self.merge(ret[-1][1], e)
            else:
                ret.append([s, e])
        return ret
