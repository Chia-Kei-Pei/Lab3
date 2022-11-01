import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    [result, int_val] = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    [result, int_val] = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_bubble_sort_invalid():
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    [result, int_val] = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_over_10_num():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 800, 900, 100, 1100]
    expected = 1

    [result, int_val_asc] = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    [result, int_val_des] = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (int_val_asc == expected and int_val_des == expected)


def test_bubble_below_10_num():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 800, 900]
    expected = 2

    [result, int_val_asc] = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    [result, int_val_des] = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (int_val_asc == expected and int_val_des == expected)


def test_bubble_0_num():
    input_arr = []
    expected = 0

    [result, int_val_asc] = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    [result, int_val_des] = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (int_val_asc == expected and int_val_des == expected)


def test_bubble_not_integers():
    input_arr = [64, 34, 25, 12.1, 22, 11, 90, 800, 900]
    expected = 3

    [result, int_val_asc] = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    [result, int_val_des] = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (int_val_asc == expected and int_val_des == expected)