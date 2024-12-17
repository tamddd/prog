class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            group["".join(sorted(s))].append(s)

        return [i[1] for i in group.items()]
