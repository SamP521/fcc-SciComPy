from arithmetic_formatter import arithmetic_arranger
import unittest
from arithmetic_formatter import arithmetic_arranger


class TestArithmeticFormatter(unittest.TestCase):
    def test_standard(self):
        problems = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_too_many_problems(self):
        problems = [
            "32 + 698",
            "3801 - 2",
            "45 + 43",
            "123 + 49",
            "988 + 40",
            "1 - 9380",
        ]
        expected = "Error: Too many problems."
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_invalid_operator(self):
        problems = ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_too_many_digits(self):
        problems = ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_only_digits(self):
        problems = ["98 + 3g8", "3801 - 2", "45 + 43", "123 + 49"]
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_show_answers(self):
        problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
        expected = "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"

        self.assertEqual(arithmetic_arranger(problems, True), expected)


if __name__ == "__main__":
    unittest.main()
