from logic_ops import *

print("=== my_and ===")
print(my_and(True, True))
print(my_and(True, False))
print(my_and(False, True))
print(my_and(False, False))

print("\n=== my_or ===")
print(my_or(True, True))
print(my_or(True, False))
print(my_or(False, True))
print(my_or(False, False))

print("\n=== my_not ===")
print(my_not(True))
print(my_not(False))

print("\n=== my_implies ===")
print(my_implies(True, True))
print(my_implies(True, False))
print(my_implies(False, True))
print(my_implies(False, False))

print("\n=== evaluate ===")
print(evaluate(("not", False)))
print(evaluate(("and", True, False)))
print(evaluate(("or", False, True)))
print(evaluate(("implies", True, False)))
print(evaluate(("and", True, ("not", False))))
print(evaluate(("implies",
                ("or", ("implies", False, False), ("not", True)),
                ("implies", ("and", True, True), ("not", False))))
)