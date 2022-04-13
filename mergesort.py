# still need to check this one out and ensure it is well written

def merge(list_a, list_b):
    i, j = 0, 0
    result = []

    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        else:
            result.append(list_b[j])
            j += 1
    
    while i < len(list_a):
        result.append(list_a[i])
        i += 1
    while j < len(list_b):
        result.append(list_b[j])
        j += 1

    return result

def mergesort(list):
    if len(list) > 1:
        mid = len(list)//2
        list_l = mergesort(list[:mid])
        list_r = mergesort(list[mid:])
        return merge(list_l, list_r)

    return list

if __name__ == '__main__':
    merge_tests = []
    merge_tests.append([[1, 2, 5, 10, 22], [2, 3, 4, 11, 12, 15, 23, 24, 25, 26]])
    merge_tests.append([[1], [0]])
    merge_tests.append([[0], [0]])
    merge_tests.append([[-100], [1, 10, 20, 50, 100]])

    sort_tests = []
    sort_tests.append([3, 2, 9, 5, 6, 1, 1, 3, 4, 8])
    sort_tests.append([0, 1, 2, 3, 4])
    sort_tests.append([4, 3, 2, 1, 0])
    sort_tests.append([0])
    sort_tests.append([-1000000])
    sort_tests.append([500, 23.234, -400000.5])
    
    print("Merge tests:")
    for test in merge_tests:
        list_a, list_b = test
        print(merge(list_a, list_b))
    print()
    print("Sort tests:")
    for test in sort_tests:
        print(mergesort(test))
