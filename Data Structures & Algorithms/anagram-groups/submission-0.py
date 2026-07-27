class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        # 1. Initialize a hash map where the key is the sorted signature and the value is a list of original strings
        hash_map = {}

        # 2. Loop through each string in `strs`
        for item in strs:
            # a. Convert the string into a sorted form to use as our key
            sorted_key = "".join(sorted(item))

            # b. If this sorted key is not yet in our dictionary, add it with an empty list
            if sorted_key not in hash_map:
                hash_map[sorted_key] = []

            # c. Append the original unsorted string to the list corresponding to this key
            hash_map[sorted_key].append(item)

        # 3. Return all the grouped lists from the dictionary values
        return list(hash_map.values())