class Solution:
    def minWindow(self, s, t):
        from collections import Counter

        need = Counter(t)
        have = {}
        left = 0
        formed = 0
        required = len(need)

        res = ""
        min_len = float('inf')

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            # shrink window
            while formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        return res