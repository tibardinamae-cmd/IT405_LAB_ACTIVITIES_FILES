
# IT 405L - Activity 1
# Logical Operators and an Expression Evaluator


# 1. AND operator
def my_and(a, b):
    if a == True:
        return b == True
    return False


# 2. OR operator
def my_or(a, b):
    if a == True:
        return True
    return b == True


# 3. NOT operator
def my_not(a):
    return a == False


# 4. IMPLIES operator
def my_implies(a, b):
    if a == True:
        return b == True
    return True


# 5. Recursive expression evaluator
def evaluate(expr):

    # Base case: return a Boolean leaf
    if isinstance(expr, bool):
        return expr

    # Get the operator
    op = expr[0]

    # Unary operator
    if op == "not":
        return my_not(evaluate(expr[1]))

    # Evaluate both operands
    left = evaluate(expr[1])
    right = evaluate(expr[2])

    # Apply the correct operator
    if op == "and":
        return my_and(left, right)

    if op == "or":
        return my_or(left, right)

    if op == "implies":
        return my_implies(left, right)

    raise ValueError("Unknown operator: " + str(op))


# TESTING THE FOUR LOGICAL OPERATORS

print("AND OPERATOR")
print(my_and(True, True))
print(my_and(True, False))
print(my_and(False, True))
print(my_and(False, False))

print("\nOR OPERATOR")
print(my_or(True, True))
print(my_or(True, False))
print(my_or(False, True))
print(my_or(False, False))

print("\nNOT OPERATOR")
print(my_not(True))
print(my_not(False))

print("\nIMPLIES OPERATOR")
print(my_implies(True, True))
print(my_implies(True, False))
print(my_implies(False, True))
print(my_implies(False, False))


# TESTING THE EXPRESSION EVALUATOR

print("\nEXPRESSION EVALUATOR")

test_expressions = [
    ("and", True, True),
    ("and", True, False),
    ("or", False, True),
    ("not", False),
    ("implies", True, False),
    ("or", True, ("and", False, True))
]

for expr in test_expressions:
    print(expr, "=", evaluate(expr))


# STEP 7: EXPECTED ERROR
print("\nSTEP 7 - EXPECTED ERROR")

try:
    evaluate(("or", True, ("and", 1/0, False)))
except Exception as error:
    print(type(error).__name__ + ": " + str(error))
