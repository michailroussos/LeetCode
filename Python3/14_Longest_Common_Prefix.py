class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=sys.maxsize
        for i in range(len(strs)):
            if len(strs[i])<min_len:
                min_len=len(strs[i])
        current=""
        for i in range(min_len):
            char=strs[0][i]
            for word in range(1,len(strs),1):
                if char!=strs[word][i]:
                    return current

            current=current+char
        return current