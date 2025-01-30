#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    bool val = true;
    // String
    char str[] = "super idol";

    // If statements
    if (x == 5) {
        printf("x is equal to 5\n");
    } else {
        printf("x is not equal to 5\n");
    }

    // For loop
    for (int i = 0; i < 5; i++) {
        printf("%d\n", i);
    }

    // While loop
    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }

    // Functions
    int c = add(5, 10);

    // Arrays
    int arr[] = {1, 2, 3, 4, 5};

    // Structs
    struct Person {
        int age;
        float height;
    };

    struct Person person1;
    person1.age = 20;
    person1.height = 170.5;

    // Dynamic Memory Allocation
    int* arr_memory = (int*) malloc(5 * sizeof(int));
    free(arr_memory);

    // Pointers
    int *ptr = &x;

    return 0;
}