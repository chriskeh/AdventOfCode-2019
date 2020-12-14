import pytest

from src.day4 import check_pw_rules


@pytest.mark.parametrize("password, expected",
                         [
                             ("22", True),
                             ("223456", True),
                             ("123455", True),
                             ("123456", False),
                             ("123450", False),
                             ("21", False),
                          ]
                         )
def test__check_pw_rules(password, expected):
    result = check_pw_rules(password)
    assert result == expected
