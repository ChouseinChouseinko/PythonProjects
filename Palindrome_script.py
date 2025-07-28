def PalindromeTwo(strParam):
    import re
    varfilters = re.sub(r'[^a-zA-Z0-9]', '', strParam).lower()
    varocg = varfilters[::-1]
    if varfilters == varocg:
        return "true"
    else:
        return "false"

    # code goes here
    return strParam


# keep this function call here
print(PalindromeTwo("Noel - sees Leon"))  # Output: "true"
print(PalindromeTwo(input("Let's try this script: ")))
