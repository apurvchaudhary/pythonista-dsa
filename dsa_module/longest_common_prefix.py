class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        _str = ""
        try:
            for i in range(len(min(strs))):
                char = None
                for j in strs:
                    if not char:
                        char = j[i]
                    elif j[i] != char:
                        raise ValueError
                _str += char
        except ValueError:
            pass
        return _str


strs = ["flower", "aiow", "flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))
