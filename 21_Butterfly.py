n = 4
# Upp
for i in range(1,n+1):
    print("*" * i+" " * (2*(n-i))+"*"*i)
# Lowe
for i in range(n-1,0,-1):
    print("*" * i + " " * (2*(n-i))+"*"* i)
