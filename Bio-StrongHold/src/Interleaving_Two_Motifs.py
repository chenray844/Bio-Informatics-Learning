def longest_common_supersequence(s, t, i, j, dp):
    if i >= len(s) and j >= len(t):
        return float('inf')
    elif i >= len(s) or j >= len(t):
        if i >= len(s):
            dp[(i, j)] = len(t) - j
            return len(t) - j
        else:
            dp[(i, j)] = len(s) - i
            return len(s) - i
    elif (i, j) in dp:
        return dp[(i, j)]
    else:
        if s[i] == t[j]:
            dp[(i, j)] = 1 + longest_common_supersequence(s, t, i + 1, j + 1, dp)
        else:
            one = longest_common_supersequence(s, t, i + 1, j, dp)
            two = longest_common_supersequence(s, t, i, j + 1, dp)
            dp[(i, j)] = 1 + min(one, two)
        return dp[(i, j)]

def reconstruct(s, t, dp):
    i, j = 0, 0
    answer = []
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            answer.append(s[i])
            i += 1
            j += 1
        else:
            one = dp.get((i + 1, j), float('inf'))
            two = dp.get((i, j + 1), float('inf'))
            if one < two:
                answer.append(s[i])
                i += 1
            else:
                answer.append(t[j])
                j += 1

    while i < len(s):
        answer.append(s[i])
        i += 1
    while j < len(t):
        answer.append(t[j])
        j += 1

    return "".join(answer)


s = "AGCAGCATCCTCTCTCGTACGCTGGAGTCGAAATGTCGTGCTAGGACATTGGTGCTTTTCAATGCTGGTCGAGGCATGACCTCACTTAGACCTGC"
t = "CTCATCTCCCGTACATCTTCAGTTATCACGAAGACAACGCTTGGACCCTCAACTGGTATTCACCCTGAAAAAGTCGAGAGTTGTCTGCTCGTGATAGAT"

dp = {}
longest_common_supersequence(s, t, 0, 0, dp)

print reconstruct(s, t, dp)