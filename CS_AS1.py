import sympy as sp
I1,I2,I3,V1,V,V0,s = sp.symbols(' I1 I2 I3 V1 V V0 s');
#Mesh equations
meq1 = (4+4*s)*I1 - (2+4*s)*I2 - 2*I3 - V
meq2 = -(2+4*s)*I1 + (14+10*s)*I2 - (4+6*s)*I3 
meq3 = -2*I1 - (4+6*s)*I2 + (6+6*s+9/s)*I3 
sol = sp.solve((meq1,meq2,meq3),(I1,I2,I3))
G1 = 8*sol[I2]/V
print(G1)

#Nodal equations
neq1 = (V1 - V)/2 + V1/(2 + 4*s) + (V1 - V0) /(4 + 6*s)
neq2 = (V0 - V1)/(4 + 6*s) + V0/8 + (V0 - V)/9*s
sol = sp.solve((neq1,neq2),(V1,V0))
G2 = sol[V0]/V
print(G2)
