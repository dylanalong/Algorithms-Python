import mergesort

def kth_smallest_sort(k, list):
    if k >= len(list) or k <= 0:
        print("k is out of bounds")
        return None
    list = mergesort.mergesort(list)
    return list[k-1]

if __name__ == '__main__':
    tests = []
    tests.append([33, 2, 54, 44, 38, 88, 21, 8, 8])

    for test in tests:
        print(kth_smallest_sort(9, test))