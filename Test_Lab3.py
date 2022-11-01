import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_over_10_num():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 800, 900, 100, 1100]
    expected = 1

    assert (Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == expected
            and Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == expected)

def test_bubble_below_10_num():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 800, 900]
    expected = 2

    assert (Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == expected
            and Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == expected)


def test_bubble_0_num():
    input_arr = []
    expected = 0

    assert (Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == expected
            and Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == expected)

def test_bubble_not_integers():
    input_arr = [64, 34, 25, 12.1, 22, 11, 90, 800, 900]
    expected = 3

    assert (Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING) == expected
            and Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING) == expected)