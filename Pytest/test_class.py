import requests
import pytest
# content of test_09.py
import time
import pytest
@pytest.mark.parametrize("test_input,expected",
                         [("3+5", 8),
                          ("2+4", 6),
                          ("6 * 9", 54),
                          ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
if __name__ == "__main__":
    pytest.main(["-vv", "test_class.py"])
