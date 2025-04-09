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


def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be equal length")
    
    differences = 0
    for a, b in zip(list1, list2):
        if a != b:
            differences += 1

    return differences / len(list1)


def get_p_distance_matrix(list_of_lists):
    size = len(list_of_lists)
    matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0.0)
            else:
                distance = get_p_distance(list_of_lists[i], list_of_lists[j])
                row.append(distance)
        matrix.append(row)

    return matrix
