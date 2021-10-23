s = "5F3Z-2e-9-w"
k = 4


def licenseKeyFormatting(s, k):
    if len(s) == 0:
        return ''
    s = s.replace("-", "").upper()
    q, r = divmod(len(s), k)
    print(q,r)
    ans = [s[:r]] if r else []
    print(ans)
    ans += (s[(r + i * k):(r + (i + 1) * k)] for i in range(q))
    return "-".join(ans)


print(licenseKeyFormatting(s, k))
