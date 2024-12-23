class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #２種類まで入れられる。
        slow = fast = 0
        vis = set()
        counter = defaultdict(int)
        c = res = 0
        while fast < len(fruits):
            vis.add(fruits[fast])
            counter[fruits[fast]] += 1
            c += 1
            while len(vis) == 3:
                counter[fruits[slow]] -= 1
                if counter[fruits[slow]] == 0:
                    vis.discard(fruits[slow])
                slow += 1
                c -= 1
            print(vis)

            res = max(res, c)
            fast += 1
        return res
