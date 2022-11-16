import numpy as np
'''
	Analitical solution for the cases
'''
psi_a = 1.0
psi_b = 0.0

fx = lambda x,psi_a,psi_b,L,gamma,q:(
   ((psi_b-psi_a)/L + (q/(2*gamma))*(L-x) )*x+psi_a
) 

## Case 1.
'''
gamma  = 1.0
l      = [0.25,0.5,0.75,1.0,1.5,2.0,3.0]
q      = 0
with open('case1.csv','a') as file:
   file.write(f'x,y,L\n')

for i in l:
    x = np.linspace(0,i)
    y = fx(x,psi_a,psi_b,i,gamma,q)
    with open('case1.csv','a') as file:
      for xx,yy in zip(x,y):
         file.write(f'{xx},{yy},{i}\n')
'''
## Case 2
'''
gamma  = 1.0
l      = [0.25,0.5,0.75,1.0,1.5,2.0,3.0]
q      = 1.0
with open('case2.csv','a') as file:
   file.write(f'x,y,L\n')

for i in l:
    x = np.linspace(0,i)
    y = fx(x,psi_a,psi_b,i,gamma,q)
    with open('case2.csv','a') as file:
      for xx,yy in zip(x,y):
         file.write(f'{xx},{yy},{i}\n')
'''
## Case 3
'''
Gamma  = [0.1,0.15,0.25,0.5,1.0,2.0,10.0]
L      = 1.0
q      = 1.0
x      = np.linspace(0,L)

with open('case3.csv','a') as file:
   file.write(f'x,y,L\n')

for i in Gamma:
    y = fx(x,psi_a,psi_b,L,i,q)
    with open('case3.csv','a') as file:
      for xx,yy in zip(x,y):
         file.write(f'{xx},{yy},{i}\n')
'''
## Case 4
with open('case4.csv','a') as file:
   file.write(f'x,y,L\n')
Gamma  = 1.0
L      = 1.0
q      = [-6.0,-4.0,-2.0,0.0,2.0,4.0,6.0]
x      = np.linspace(0,L)
for i in q:
    y = fx(x,psi_a,psi_b,L,Gamma,i)
    with open('case4.csv','a') as file:
      for xx,yy in zip(x,y):
         file.write(f'{xx},{yy},{i}\n')
