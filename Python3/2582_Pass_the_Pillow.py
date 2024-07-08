class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        cycle_length = 2 * (n - 1)
    
        eff_time = time % cycle_length
  
        if eff_time < n:
        
            return eff_time + 1
        else:
            return 2 * n - eff_time - 1