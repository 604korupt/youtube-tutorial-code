#include <iostream>
#include <string>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    std::string name = "super idol";
    // Strings can be an array of characters
    char nameArray[] = "super idol";

    // If statements
    if (x == 5) {
        std::cout << "x is 5" << std::endl;
    } else {
        std::cout << "x is not 5" << std::endl;
    }

    // For loop
    for (int i = 0; i < 5; i++) {
        std::cout << i << std::endl;
    }

    // While loop
    int i = 0;
    while (i < 5) {
        std::cout << i << std::endl;
        i++;
    }

    // Functions
    int c = add(5, 10);

    // Arrays
    int arr[] = {1, 2, 3, 4, 5};

    // Structs
    struct Person {
        std::string name;
        int age;
    };

    Person p;
    p.name = "Super Idol";
    p.age = 20;

    // Dynamic Memory Allocation
    int *memory = new int[5];
    delete[] memory;

    // Pointers
    int *ptr = &x;

    // Classes
    class Car {
        public:
            std::string brand;
            std::string model;
            int year;
            Car(std::string brand, std::string model, int year) {
                this->brand = brand;
                this->model = model;
                this->year = year;
            }
    };

    Car car = Car("Ford", "Mustang", 1969);

    return 0;
}