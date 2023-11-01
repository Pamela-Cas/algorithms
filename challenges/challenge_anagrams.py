def sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        sort(numbers, start, p - 1)
        sort(numbers, p + 1, end)


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for i in range(start, end):
        if numbers[i] <= pivot:
            delimiter = delimiter + 1
            numbers[i], numbers[delimiter] = numbers[delimiter], numbers[i]

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    sort(first_list, 0, len(first_list) - 1)
    first_str = "".join(first_list)
    sort(second_list, 0, len(second_list) - 1)
    second_str = "".join(second_list)

    if first_str != second_str:
        return (first_str, second_str, False)
    if first_str == "" or second_str == "":
        return (first_str, second_str, False)
    return (first_str, second_str, True)
