
from itertools import product
from logic_ops import evaluate
import re

# Convert string expressions into tuple expressions
def parse_expression(expr):
    if not isinstance(expr, str):
        return expr

    tokens = re.findall(r'\(|\)|and|or|not|implies|[p-z]', expr)
    tokens = [t for t in tokens if t.strip()]

    def parse():
        token = tokens.pop(0)

        if token == '(':
            left = parse()
            op = tokens.pop(0)

            if op == 'not':
                result = ('not', parse())
            else:
                right = parse()
                result = (op, left, right)

            tokens.pop(0)
            return result

        return token

    return parse()

# FUNCTION 1: Generate all possible assignments
def assignments(variables):
    return [
        dict(zip(variables, values))
        for values in product([True, False], repeat=len(variables))
    ]


# FUNCTION 2: Substitute variable values into an expression
def fill(expr, assignment):

    if isinstance(expr, str):
        return assignment[expr]

    if isinstance(expr, bool):
        return expr

    if isinstance(expr, tuple):
        return tuple(
            [expr[0]] +
            [fill(x, assignment) for x in expr[1:]]
        )

    return expr


# FUNCTION 3: Generate and display a truth table
def truth_table(expr, variables):

    expr = parse_expression(expr)

    rows = assignments(variables)    
    results = []

    print(" | ".join(variables) + " | Result")
    print("-" * 35)

    for assignment in rows:

        values = [
            str(assignment[v])
            for v in variables
        ]

        result = evaluate(fill(expr, assignment))
        results.append(result)

        print(" | ".join(values) + " | " + str(result))

    return results


# FUNCTION 4: Check logical equivalence
def equivalent(expr1, expr2, variables):

    expr1 = parse_expression(expr1)
    expr2 = parse_expression(expr2)

    for assignment in assignments(variables):

        value1 = evaluate(fill(expr1, assignment))
        value2 = evaluate(fill(expr2, assignment))

        if value1 != value2:
            return False

    return True
