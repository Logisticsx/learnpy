r5=15000
r6=20000
r7=25000
r8=30000
r9=35000
r10=40000
r11=45000
r12=50000
r13=55000

i = 0.15
q = 0.14

r5o = r5 + 5000 * q
r6n = r6 + 5000 * i

x=r6n - r5o * (1-q)

print (x)
