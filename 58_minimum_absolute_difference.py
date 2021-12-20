class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # [1,2,3,4]
        #    ^
        #  
        # seen = {4,2}
        # curr_min = 1
        # {2:[[2,4]], 1:[[3,4],[2,3],[1,2]]}
        
        arr.sort()
        
        curr_min = None
        ret = []
        for i in range(1,len(arr)):
            diff = arr[i]-arr[i-1]
            if not curr_min or diff < curr_min:
                curr_min = diff
                ret = []
            if diff == curr_min:
                ret.append([arr[i-1], arr[i]])
                
        return ret
                
        
        