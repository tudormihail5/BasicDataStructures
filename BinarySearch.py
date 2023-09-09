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


def main():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    a = search1(l, 8, 0, len(l) - 1)
    b = search2(l, 8, 0, len(l) - 1)
    print(a)
    print(b)


main() 