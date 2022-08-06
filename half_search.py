# 二分查找


def half_search(search, target):
    """
    :param target:
    :param search:
    :return:
    """
    l, r = 0, len(search) - 1
    while l <= r:
        mid_index = l + (r - l) // 2
        if search[mid_index] == target:
            return mid_index
        elif search[mid_index] < target:
            l = mid_index + 1
        else:
            r = mid_index - 1


def half_search_left_boundary(search, target):
    """
    左边界
    :param target:
    :param search:
    :return:
    """
    l, r = 0, len(search)
    while l < r:
        mid_index = l + ((r - l) // 2)
        if search[mid_index] == target:
            r = mid_index
        elif search[mid_index] < target:
            l = mid_index + 1
        else:
            r = mid_index
    return l


def half_search_left_boundary2(search, target):
    """
    左边界
    :param target:
    :param search:
    :return:
    """
    l, r = 0, len(search) - 1
    while l <= r:
        mid_index = l + ((r - l) // 2)
        if search[mid_index] == target:
            r = mid_index - 1
        elif search[mid_index] < target:
            l = mid_index + 1
        else:
            r = mid_index - 1
    return l


if __name__ == '__main__':
    a = [4, 5, 6, 7, 8, 9, 10, 11]
    print(half_search(a, 7))
    a = [4, 5, 6, 9, 9, 9, 10, 11]
    print(half_search_left_boundary(a, 9))
    print(half_search_left_boundary2(a, 9))
