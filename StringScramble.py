def StringScramble(str1, str2):
    from collections import Counter
    varfilters = Counter(str1)
    varocg = Counter(str2)

    for char in varocg:
        if varocg[char] > varfilters.get(char, 0):
            return "false"

    return "true"

    # code goes here
    return str1


# keep this function call here
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(StringScramble(str1, str2))
