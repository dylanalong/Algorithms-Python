def swap(list, i, j):
    try:
        list[i], list[j] = list[j], list[i]
    except TypeError as e:
        print("Swap function error:", e)
    return list

# Lists and dictionaries are passed by reference, but built-in
# types like int, bool, float, string are passed by value.
# These built-in types are immutable. When you "change" them it
# will actually create a new object; the previous object will not
# be changed.
def partition(list):
    pivot = list[0]
    i = 1
    j = len(list) - 1

    while i < j:
        while list[i] <= pivot:
            i += 1
            if i >= len(list)-1:
                break
        while list[j] > pivot:
            j -= 1
            if j < 1:
                break
        if i < j:
            swap(list, i, j)
    
    list = swap(list, 0, j)
    return j

def quicksort(list):
    if len(list) <= 1:
        return list
    if len(list) == 2:
        if list[0] > list[1]:
            return [list[1], list[0]]
        return list

    pos = partition(list)

    r_list = []
    l_list = []

    if pos < len(list) - 1:
        r_list = quicksort(list[pos+1:])
    if pos > 0:
        l_list = quicksort(list[:pos])

    return l_list + [list[pos]] + r_list


if __name__ == '__main__':
    tests = []
    tests.append([6, 4, 1, 2, 9, 7, 3, 4, 10, 2])
    tests.append([0])
    tests.append([100000000])
    tests.append([1, 2, 3, 4, 5])
    tests.append([5, 4, 3, 2, 1])
    tests.append([-1000000, 2, 4.56])

    for test in tests:
        print("before:", test)
        print("sorted:", quicksort(test))
        print()