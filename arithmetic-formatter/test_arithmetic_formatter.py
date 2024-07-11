from arithmetic_formatter import arithmetic_arranger
import pytest


def test_standard():
    assert arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) == "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"


def test_too_many_problems():
    assert arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "988 + 40", "1 - 9380"]) == "Error: Too many problems."


def test_invalid_operator():
    assert arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) == "Error: Operator must be '+' or '-'."


def test_too_many_digits():
    assert arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) == "Error: Numbers cannot be more than four digits."


def test_only_digits():
    assert arithmetic_arranger(["98 + 3g8", "3801 - 2", "45 + 43", "123 + 49"]) == "Error: Numbers must only contain digits."


def test_show_answers():
    assert arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True) == "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"
