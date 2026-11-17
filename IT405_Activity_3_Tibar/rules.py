
# IT 405L - Activity 3
# A Rule Engine: Facts, Rules, Queries and Backward Chaining

# STEP 1: Represent the eight family facts as tuples.
# Each fact has the form ('parent', older_person, younger_person).

FACTS = [
    ('parent', 'jom', 'ben'),
    ('parent', 'jom', 'tino'),
    ('parent', 'ben', 'ivy'),
    ('parent', 'tino', 'ana'),
    ('parent', 'ben', 'olen'),
    ('parent', 'ana', 'carl'),
    ('parent', 'olen', 'hugo'),
    ('parent', 'carl', 'uma'),
]

# STEP 4: Represent rules as a head and a list of conditions.

RULES = [
    (
        ('grandparent', 'X', 'Z'),
        [
            ('parent', 'X', 'Y'),
            ('parent', 'Y', 'Z')
        ]
    ),

    # STEP 7: An ancestor is a parent.
    (
        ('ancestor', 'X', 'Y'),
        [
            ('parent', 'X', 'Y')
        ]
    ),

    # STEP 7: An ancestor is also a parent of an ancestor.
    (
        ('ancestor', 'X', 'Z'),
        [
            ('parent', 'X', 'Y'),
            ('ancestor', 'Y', 'Z')
        ]
    )
]


# Identify a variable.
def is_var(term):
    return isinstance(term, str) and term[:1].isupper()


# STEP 2: Match a pattern against a fact.
# Return a dictionary of bindings, or None if they do not match.

def matches(pattern, fact, bindings=None):
    if bindings is None:
        bindings = {}

    result = bindings.copy()

    if len(pattern) != len(fact):
        return None

    for p, f in zip(pattern, fact):
        if is_var(p):
            if p in result:
                if result[p] != f:
                    return None
            else:
                result[p] = f
        elif p != f:
            return None

    return result


# Replace variables with their current values.
def substitute(term, bindings):
    return tuple(bindings.get(item, item) for item in term)


# Give rule variables new names each time a rule is used.
# This prevents variables from different rule applications
# from accidentally sharing bindings.

def fresh_rule(rule):
    global rule_number
    rule_number += 1

    head, conditions = rule
    replacements = {}

    def rename(term):
        if is_var(term):
            if term not in replacements:
                replacements[term] = term + "_" + str(rule_number)
            return replacements[term]
        return term

    new_head = tuple(rename(item) for item in head)

    new_conditions = [
        tuple(rename(item) for item in condition)
        for condition in conditions
    ]

    return new_head, new_conditions


rule_number = 0


# Solve several conditions using the same bindings.

def solve_conditions(conditions, bindings, facts, depth):
    if not conditions:
        yield bindings
        return

    first = conditions[0]
    remaining = conditions[1:]

    for result in solve_goal(first, bindings, facts, depth + 1):
        yield from solve_conditions(
            remaining, result, facts, depth + 1
        )


# Solve one goal by trying facts first, then rules.
# The depth limit helps detect recursive cycles.

def solve_goal(goal, bindings, facts, depth=0):
    if depth > 60:
        raise RuntimeError(
            "Search depth exceeded 60. A recursive cycle may exist."
        )

    goal = substitute(goal, bindings)

    # First, try matching the goal against facts.
    for fact in facts:
        result = matches(goal, fact, bindings)

        # IMPORTANT: {} is a successful match.
        if result is not None:
            yield result

    # Next, try matching the goal against rule heads.
    for rule in RULES:
        head, conditions = fresh_rule(rule)

        result = matches(head, goal, bindings)

        if result is not None:
            yield from solve_conditions(
                conditions, result, facts, depth + 1
            )


# STEP 5: Query returns every set of bindings satisfying the goal.

def query(goal, facts=None):
    if facts is None:
        facts = FACTS

    return list(solve_goal(goal, {}, facts))


# STEP 3: Test matches against the parent facts.
if __name__ == "__main__":

    print("STEP 3: MATCHING PARENT OF BEN")

    for fact in FACTS:
        result = matches(('parent', 'X', 'ben'), fact)

        if result is not None:
            print(result)

    # STEP 6: Ask for all grandparents.
    print("\nSTEP 6: ALL GRANDPARENTS")

    for answer in query(('grandparent', 'X', 'Z')):
        print({
            'X': answer['X'],
            'Z': answer['Z']
        })

    # STEP 7: Ask for all ancestors.
    print("\nSTEP 7: ALL ANCESTORS")

    for answer in query(('ancestor', 'X', 'Z')):
        print({
            'X': answer['X'],
            'Z': answer['Z']
        })

# STEP 8 is run separately using the personal parameter file.
