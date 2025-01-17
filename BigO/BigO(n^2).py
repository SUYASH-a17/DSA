def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(5)
# Less efficient than BigO(n) from time complexity pov

# BigO(n^2 + n) will be BigO(n^2) too as the n increases the standalone n becomes insignificant.
# So we drop the non dominant constant

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
            print(k)

print_items(5)