def square(x):
    return x*x

def cube(x):
    return x*x*x

for i in range(10):
    print("---")
    print(f"{i} squared is {square(i)}")
    print(f"{i} cubed is {cube(i)}")
    print("---")