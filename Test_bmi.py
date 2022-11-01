import Lab2.bmi as bmi


def test_bmi_normal_weight():
    assert (bmi.calculate_bmi(1.75, 57) == 0 and bmi.calculate_bmi(1.75, 76.5) == 0)


def test_bmi_over_weight():
    assert (bmi.calculate_bmi(1.75, 77) == 1)


def test_bmi_under_weight():
    assert (bmi.calculate_bmi(1.75, 56) == -1)