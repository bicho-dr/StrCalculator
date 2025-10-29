from src.StrCalculate import StrCalculate


def test_function():
   StrCalculate()

def test_return_empty():
    assert StrCalculate("") == 0