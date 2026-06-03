class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = {}
        results = []
        for s in strs:
            key = "".join(sorted(s))
            if key not in grams:
                grams[key] = []
            grams[key].append(s)
        for key in grams:
            results.append(grams[key])
        return results


        