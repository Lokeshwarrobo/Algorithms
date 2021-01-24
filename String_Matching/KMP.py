# Time Complexcity  : O(M + N)
# Space Complexcity : O(N)

text = "ABABDABACDABABCABABCABAB"  # M
pat = "ABABCABAB"                  # N

def kmp(text, pat):
    m = len(text)
    n = len(pat)
    t = map(pat)
    i = j = 0
    while i != m:
        if text[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = t[j - 1]
            else:
                i += 1
        if j == n:
            print(i - j)
            j = t[j - 1]

def map(pat):
    t = [0] * len(pat)
    n = 0
    m = 1
    while m != len(pat):
        if pat[m] == pat[n]:
            n += 1
            t[m] = n
            m += 1
        elif n != 0:
            n = t[n - 1]
        else:
            t[m] = 0
            m += 1
    return t

kmp(text, pat)

