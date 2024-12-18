class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        ret = []

        for i in p:
            if i == "" or i == ".": continue
            elif i == "..":
                if len(ret) == 0:continue
                ret.pop()
            else:
                ret.append("/" + i)

        if len(ret) == 0:
            ret.append("/")
        return "".join(ret)
