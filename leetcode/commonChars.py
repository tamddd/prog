class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ret = Counter(words[0])
        
        for word in words[1:]:
            counter = Counter(word)
            for char in ret.keys():
                ret[char] = min(ret[char], counter[char])
        
        return [char for char, count in ret.items() for _ in range(count)]
