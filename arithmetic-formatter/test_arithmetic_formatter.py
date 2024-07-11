from arithmetic_formatter import arithmetic_arranger


def test_standard():
    problems = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
    expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
    assert arithmetic_arranger(problems) == expected


def test_too_many_problems():
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "988 + 40", "1 - 9380"]
    expected = "Error: Too many problems."
    assert arithmetic_arranger(problems) == expected


def test_invalid_operator():
    problems = ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
    expected = "Error: Operator must be '+' or '-'."
    assert arithmetic_arranger(problems) == expected


def test_too_many_digits():
    problems = ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]
    expected = "Error: Numbers cannot be more than four digits."
    assert arithmetic_arranger(problems) == expected


def test_only_digits():
    problems = ["98 + 3g8", "3801 - 2", "45 + 43", "123 + 49"]
    expected = "Error: Numbers must only contain digits."
    assert arithmetic_arranger(problems) == expected


def test_show_answers():
    problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
    expected = "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"
    assert arithmetic_arranger(problems, True) == expected
