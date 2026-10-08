import sympy as sp
p12, p13, p14, p15, p23, p24, p25, p34, p35, p45 = sp.symbols(
    'p12 p13 p14 p15 p23 p24 p25 p34 p35 p45', real=True)
P = sp.Matrix([[1, -p12, -p13, -p14, -p15], [-p12, 1, -p23, -p24, -p25], [-p13, -
              p23, 1, -p34, -p35], [-p14, -p24, -p34, 1, -p45], [-p15, -p25, -p35, -p45, 1]])
A = P.adjugate()
A11 = A[0, 0]
A22 = A[1, 1]
A33 = A[2, 2]
A44 = A[3, 3]
A55 = A[4, 4]
A12 = A[0, 1]
A13 = A[0, 2]
A14 = A[0, 3]
A15 = A[0, 4]
A23 = A[1, 2]
A24 = A[1, 3]
A25 = A[1, 4]
A34 = A[2, 3]
A35 = A[2, 4]
A45 = A[3, 4]
r12 = A12/sp.sqrt(A11*A22)
r13 = A13/sp.sqrt(A11*A33)
r14 = A14/sp.sqrt(A11*A44)
r15 = A15/sp.sqrt(A11*A55)
r23 = A23/sp.sqrt(A22*A33)
r24 = A24/sp.sqrt(A22*A44)
r25 = A25/sp.sqrt(A22*A55)
r34 = A34/sp.sqrt(A33*A44)
r35 = A35/sp.sqrt(A33*A55)
r45 = A45/sp.sqrt(A44*A55)
print(sp.factor(r12))
