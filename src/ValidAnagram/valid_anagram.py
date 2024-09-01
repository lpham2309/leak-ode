def isAnagram(s: str, t:str) -> bool:
    result = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] not in result:
            result[s[i]] = 1
        else:
            result[s[i]] += 1

    for j in range(len(t)):
        if t[j] not in result:
            result[t[j]] = 1
        else:
            result[t[j]] += 1

    for k, v in result.items():
        if v != 0:
            return False
    return True
