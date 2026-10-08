import sympy as sp
p12, p13, p23 = sp.symbols('p12 p13 p23', real=True)
P = sp.Matrix([[1, -p12, -p13], [-p12, 1, -p23], [-p13, -p23, 1]])
A = P.adjugate()
A11 = A[0, 0]
A22 = A[1, 1]
A33 = A[2, 2]
A12 = A[0, 1]
A13 = A[0, 2]
A23 = A[1, 2]
r12 = A12/sp.sqrt(A11*A22)
r13 = A13/sp.sqrt(A11*A33)
r23 = A23/sp.sqrt(A22*A33)
print(f"r12={r12},r13={r13},r23={r23}")
