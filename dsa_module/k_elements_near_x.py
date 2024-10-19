a, k, x = [1, 3, 4, 7, 9, 10, 17, 19, 23, 29], 5, 19


def binary_search(arr, low, high, findx):
    # O(logN) - time
    # O(logN) - space
    if low <= high:
        mid = (high + low) // 2
        if findx == arr[mid]:
            return mid
        elif findx > arr[mid]:
            return binary_search(arr, mid + 1, high, findx)
        else:
            return binary_search(arr, low, mid - 1, findx)
    raise IndexError("No element found")


index = binary_search(a, 0, len(a) - 1, x)
left, right, b = index, index + 1, []

while k > 0:
    # O(K) - time
    # O(KN) - space
    if left < 0:
        b.append(a[right])
        right += 1
    else:
        b.insert(0, a[left])
        left -= 1
    k -= 1
    if k == 0:
        continue
    if right > len(a) - 1:
        b.insert(0, a[left])
        left -= 1
    else:
        b.append(a[right])
        right += 1
    k -= 1
print(b)
