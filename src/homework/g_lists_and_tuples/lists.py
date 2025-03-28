def get_lowest_list_value(lst):
    lowest = lst[0]
    for num in lst:
        if num < lowest:
            lowest = num
    return lowest


def get_highest_list_value(lst):
    highest = lst[0]
    for num in lst:
        if num > highest:
            highest = num
    return highest