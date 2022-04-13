def kth_smallest_quickselect(k, list):
    index = partition(list)
    if index == k-1:
        return list[index]
    if index < k-1:
        return kth_smallest_quickselect(k-len(list[:index+1]), list[index+1:])
    return kth_smallest_quickselect(k, list[:index])

def partition(list):
    i = 0
    j = len(list)-2
    pivot = list[len(list)-1]
    while i <= j:
        if list[i] > pivot and list[j] <= pivot:
            swap(i, j, list)
        if list[i] <= pivot:
            i += 1
        if list[j] > pivot:
            j -= 1
    swap(i, len(list)-1, list)
    return i

def swap(i, j, list):
    list[i], list[j] = list[j], list[i]

if __name__ == '__main__':
    tests = []
    tests.append([3, 8, 7, 1, 5, 2, 6, 4])

    for test in tests:
        print(kth_smallest_quickselect(3, test))