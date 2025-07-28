def SimpleMode(arr):
    mode_dict = {}
    max_count = 0
    mode = -1

    for num in arr:
        if num in mode_dict:
            mode_dict[num] += 1
        else:
            mode_dict[num] = 1

        if mode_dict[num] > max_count:
            mode = num
            max_count = mode_dict[num]

    if max_count == 1:
        return -1

    return mode


# keep this function call here
print(SimpleMode(
    list(map(int, input("Please enter numbers separated by commas: ").split(',')))))
