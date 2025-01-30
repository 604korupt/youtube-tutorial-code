# Takes another function as a parameter
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def double(x):
    return 2 * x

def add_func(x, func):
    total = 0
    for i in range(1, x + 1):
        total += func(i)
    return total

add_func(3, square) # returns (1 ** 2) + (2 ** 2) + (3 ** 2) = 14
add_func(3, cube) # returns (1 ** 3) + (2 ** 3) + (3 ** 3) = 36
add_func(3, double) # returns (2 * 1) + (2 * 2) + (2 * 3) = 12

# Returns a function as a result
def multiply(x):
    def mul(y):
        return x * y
    return mul

func_result = multiply(3) # returns a function, which is mul
func_result(2) # returns 3 * 2