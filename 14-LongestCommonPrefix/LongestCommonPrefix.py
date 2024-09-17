class Solution(object):
    def longestCommonPrefix(strs):
        # go through the first letter of each item in the list. if the index contains the same letter, append to prefix
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return prefix
        return prefix




print(Solution.longestCommonPrefix(["test", "test2", "tesseract"]))

            

            
