def test_func_1(a, b):
    return a + b

def test_func_2(a):
    return a + 3

if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    X = test_func_1(a, b)
    res = test_func_2(X)
    print(res)
