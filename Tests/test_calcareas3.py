import pytest
from calcareas3 import calculate_rectangle_area


def test_calc_rec_area():
    assert calculate_rectangle_area(10, 20) == 200



pytest.main(["-v", "--tb=line", "-rN", __file__])