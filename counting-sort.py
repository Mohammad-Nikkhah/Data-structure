def counting_sort(arr):
    maximum = max(arr) + 1
    helper_list = [0] * maximum

    s_list = []
    for value in arr:
        helper_list[value] = helper_list[value] + 1

    for j in range(len(helper_list)):
        s_list.extend([j] * helper_list[j])
    return s_list


print(counting_sort([68, 32, 45, 122, 5, 6577, 1313, 219, 140, 23, 4, 542, 1]))

