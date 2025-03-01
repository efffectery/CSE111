import json
import pytest
from currancy_convert import calculte_converted_amount, get_api_data

def test_currency_conversions():
    """THE TESTS WILL/MIGHT FAIL BECAUSE THE EXCHANCGE RATES CHANGE OVER TIME
    This API is either super acurate or super terrible because google and this api 
    have extremly different exchange rates so one is faster then the other"""
    assert calculte_converted_amount(50, "EUR") == pytest.approx(48.65, abs=20)
    assert calculte_converted_amount(100, "USD") == pytest.approx(112.00, abs=15)
    assert calculte_converted_amount(10, "GBP") == pytest.approx(8.20, abs=3)
    assert calculte_converted_amount(200, "JPY") == pytest.approx(30030.00, abs=1500)
    assert calculte_converted_amount(150, "USD") == pytest.approx(168.00, abs=20)
    assert calculte_converted_amount(30, "GBP") == pytest.approx(24.60, abs=5)
    assert calculte_converted_amount(75, "JPY") == pytest.approx(11261.25, abs=1000)

def test_get_api_data():
    """Testing if the expected keys are in the data extracted from the api"""
    assert "base" and "date" and "rates" in get_api_data()
    assert "USD" in get_api_data()["rates"]
    assert isinstance(get_api_data()["rates"], dict)
    assert isinstance(get_api_data(), dict)


pytest.main(["-v", "--tb=line", "-rN", __file__])