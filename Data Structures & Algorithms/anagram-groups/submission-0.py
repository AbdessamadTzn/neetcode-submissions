from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        temp = defaultdict(list)
        for word in strs:
            temp[str(sorted(word))].append(word)

        my_list = list(temp.values())
        
        
        return my_list

            
        
        