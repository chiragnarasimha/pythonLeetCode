def longestCommonPrefix(strs: [str]) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        while prefix != strs[i][0:(len(prefix))]:
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


longestCommonPrefix(["flower", "flow", "flight"])
