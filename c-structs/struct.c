#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct SuperIdol {
    int age;
    double height;
    char name[50];
}

typedef struct {
    int age;
    double height;
    char name[50];
} SuperIdol2;

int main() {
    struct SuperIdol superIdol1;
    // Assign values to struct fields
    superIdol1.age = 18;
    superIdol1.height = 170.5;

    struct SuperIdol superidol2 = {20, 175.5, "Super Idol 2"};

    // Use strcpy to assign strings
    strcpy(superIdol1.name, "Super Idol 1");

    // Creating a struct using dynamic memory allocation
    struct SuperIdol *superIdol3 = malloc(sizeof(struct SuperIdol));
    if (superIdol3 == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    // Assign values using arrow notation
    superIdol3->age = 22;
    superIdol3->height = 180.5;
    strcpy(superIdol3->name, "Super Idol 3");

    printf("Super Idol 1: %s, %d, %.2f\n", superIdol1.name, superIdol1.age, superIdol1.height);
    printf("Super Idol 2: %s, %d, %.2f\n", superIdol2.name, superIdol2.age, superIdol2.height);
    printf("Super Idol 3: %s, %d, %.2f\n", superIdol3->name, superIdol3->age, superIdol3->height);

    free(superIdol3);

    return 0;
}