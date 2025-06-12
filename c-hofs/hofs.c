#include <stdio.h>

// Takes another function as a parameter
int square(int x) {
    return x * x;
}

int double_num(int x) {
    return x * 2;
}

int add_function(int (*func)(int), int x) {
    int total = 0;
    for (int i = 1; i <= x; i++) {
        total += func(i);
    }
    return total;
}

// Returns a function as a result
int multiply(int x, int y) {
    return x * y;
}

int (*get_mul_func())(int, int) {
    return multiply;
}

// function currying
typedef int (*operation_func)(int);

operation_func add(int x) {
    int add_func(int y) {
        return x + y;
    }
    return add_func;
}

int main() {
    int result = add_function(square, 3); // 1^2 + 2^2 + 3^2 = 14
    int result2 = add_function(double_num, 3); // 1*2 + 2*2 + 3*2 = 12

    int (*multiply_func)(int, int) = get_mul_func(); // returns function pointer
    int product = multiply_func(3, 4); // returns 3 * 4
    
    operation_func add_5 = add(5); // returns a function
    int num = add_5(3); // returns 5 + 3

    return 0;
}