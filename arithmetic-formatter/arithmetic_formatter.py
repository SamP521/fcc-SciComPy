def main():
    # Example Case
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    problem_list = [equation.split(' ') for equation in problems]
    operators = ["+", "-"]
    line1 = []
    line2 = []
    dashes = []
    results = []

    for equation in problem_list:
        first = equation[0]
        second = equation[2]
        operator = equation[1]

        if operator not in operators:
            return "Error: Operator must be '+' or '-'."
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == '+':
            result = str(int(first) + int(second))
        else:
            result = str(int(first) - int(second))

        line1.append(" " * (eq_length(equation) - len(first)) + first)
        line2.append(operator + " " * (eq_length(equation) - len(second) - 1) + second)
        dashes.append("-" * eq_length(equation))
        results.append(" " * (eq_length(equation) - len(result)) + result)

    adj_line1 = "    ".join(line1)
    adj_line2 = "    ".join(line2)
    adj_dashes = "    ".join(dashes)
    adj_results = "    ".join(results)

    if show_answers:
        return "\n".join([adj_line1, adj_line2, adj_dashes, adj_results])

    return "\n".join([adj_line1, adj_line2, adj_dashes])

def eq_length(equation):
    return max(len(equation[0]), len(equation[2])) + 2

if __name__ == "__main__":
    main()
