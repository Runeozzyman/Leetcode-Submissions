class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l, r = 0, 0
        
        have = defaultdict(int)
        have_count = 0 #count how many char freqs we've met

        need = defaultdict(int)
        minString = ""
        minLen = float('inf')

        for char in t:
            need[char] += 1
        
        need_count = len(need)

        for r in range(len(s)):
            char = s[r]
            if char in need:
                have[char] += 1
                if have[char] == need[char]:
                    have_count += 1

            while have_count == need_count:
                curr_string = s[l:r+1]
                if len(curr_string) < minLen:
                    minString = curr_string
                    minLen = len(minString)

                char = s[l]

                if char in need:
                    have[char] -= 1

                    if have[char] < need[char]:
                        have_count -= 1
                
                l += 1
            
        
        return minString