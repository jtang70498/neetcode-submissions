class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # loop through indices of first item
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check this character against every other string in the list
            for s in strs:
                # If index is out of bounds or characters don't match...
                if i == len(s) or s[i] != char:
                    # Return whatever common prefix we've found so far
                    return strs[0][:i]
                    
        return strs[0]