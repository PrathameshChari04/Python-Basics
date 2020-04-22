def square(x):
    return x*x

def cube(x):
    return x*x*x

def main():
    for i in range(10):
        print("---")
        print(f"{i} squared is {square(i)}")
        print(f"{i} cubed is {cube(i)}")
        print("---")


if __name__ == "__main__":
    main()