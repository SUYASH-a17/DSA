# BigO(a+b)
# 2 different inputs a and b can be considered as 2 different loops and we can add them together. 
# But the addition will be a+b not 2n because the inputs are different a,b =! n
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

print_items(5, 7)

# Similarly, BigO(a*b) is the TC for nested for loops
# BigO(a*b)
def print_items(c, d):
    for i in range(c):
        for j in range(d):
            print(i, j)

print_items(2, 5)