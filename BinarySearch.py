def search1(l, x, low, high):
    if low <= high:
        mid = int((low + high) / 2)
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            return search1(l, x, low, mid - 1)
        else:
            return search1(l, x, mid + 1, high)
    else:
        return -1


def search2(l, x, low, high):
    while low <= high:
        mid = int((low + high) / 2)
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
