#q1
# Logical functions
def implies(p, q):
    return not p or q

def contrapositive(p, q):
    return implies(not q, not p)

def converse(p, q):
    return implies(q, p)

def inverse(p, q):
    return implies(not p, not q)

def biconditional(p, q):
    return p == q

def xor(p, q):
    return (p or q) and (not (p and q))

# Logical equivalences
def distributive(p, q, r):
    return implies(p or q, r) == (implies(p, r) and implies(q, r))

def exportation(p, q, r):
    return implies(p and q, r) == implies(p, implies(q, r))

def reduction(p, q):
    return not implies(p, q) == (p and not q)

def equivalence(p, q):
    return biconditional(p, q) == (not xor(p, q))

def truthTable():
    # Columns
    col1 = 'p'
    col2 = 'q'
    col3 = 'r'
    col4 = 'p or q'
    col5 = '(p or q) -> r'
    col6 = 'p -> r'
    col7 = 'q -> r'
    col8 = '(p -> r) <-> (q -> r)'
    print(f'{col1} \t{col2} \t{col3} \t{col4} \t{col5} \t{col6} \t{col7} \t{col8}')
    print('-' * 90)
    # Iteration of proposition values
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                col1 = p
                col2 = q
                col3 = r
                col4 = p or q
                col5 = implies((p or q), r)
                col6 = implies(p, r)
                col7 = implies(q, r)
                col8 = implies(p, r) == implies(q, r)
                print(f'{col1} \t{col2} \t{col3} \t{col4} \t{col5} \t{col6} \t{col7} \t{col8}')

truthTable()


#q2  # Task: Modify values for p and q

p = True
q = True
# Example:
print(not xor(p, q))
print(biconditional(p, q))


#q3
def proposition_to_string(p, q):
    prop = f"If {p}, then {q}."
    return prop

def main():
    p = "it rains"
    q = "the ground is wet"
    print("Original Proposition: ", proposition_to_string(p, q))
    p_inv = "it does not rain"
    q_inv = "the ground is not wet"
    print("Inverse: ", proposition_to_string(p_inv, q_inv))
    print("Converse: ", proposition_to_string(q, p))
    print("Contrapositive: ", proposition_to_string(q_inv, p_inv))

main()

