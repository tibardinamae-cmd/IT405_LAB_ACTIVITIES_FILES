from rules import query, FACTS

print("STEP 8: TESTING THE EXTRA FACT")

# Add the extra fact: ana is her own parent.
step8_fact = ('parent', 'ana', 'ana')
step8_facts = FACTS + [step8_fact]

# Test the recursive ancestor rule.
try:
    answers = query(('ancestor', 'ana', 'Z'), facts=step8_facts)
    print("ANCESTOR RESULTS:", answers)

except RuntimeError as error:
    print("ERROR:", error)


1. What happened after adding the extra fact?

The extra fact ('ana', 'ana') created a self-referencing relationship because Ana became her own parent. The recursive ancestor rule kept searching for the same relationship repeatedly. The program reached the depth limit of 60 and stopped with an error message.

2. Why did this happen?

It happened because the recursive rule continued calling itself without reaching a stopping condition.

3. How can the engine be improved?

The engine can be improved by tracking previously visited goals to prevent repeating the same search and avoid infinite recursion.