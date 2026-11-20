def longest_palindrome(s):
    start = 0
    size = 0
    for i in range(len(s)):
        for j in (i, i + 1):
            l = i
            r = j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > size:
                    start = l
                    size = r - l + 1
                l -= 1
                r += 1
    return s[start:start + size]
