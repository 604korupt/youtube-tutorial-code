#include <iostream>
#include <string>

class Penguin {
    // Anything below the private keyword is only accessible from within the class
    private:
        int health;
        int speed;
        int power;

    // Anything below the protected keyword is accessible from within the class and derived classes
    protected:
        std::string type;

    // Anything below the public keyword is accessible from outside the class
    public:
        std::string name;

        Penguin() : health(100), speed(10), power(20), name("Dan") {}

        Penguin(int initialHealth, int initialSpeed, int initialPower) {
            health = initialHealth;
            speed = initialSpeed;
            power = initialPower;
        }

        void move() {
            std::cout << "Penguin is moving at speed " << speed << std::endl;
        }

        void attack() {
            std::cout << "Penguin is attacking with power " << power << std::endl;
        }

        // Must be declared to be accessible from outside the class
        int getHealth();
};

int Penguin::getHealth() {
    return health;
}

int main() {
    Penguin pengun;
    pengun.name = "Pengun";
    pengun.move();

    Penguin pengun2(100, 10, 20);
    pengun2.move();
    int health = pengun2.getHealth();

    Penguin *pengun3 = new Penguin(100, 20, 30);
    pengun3->name = "Super Idol";
    pengun3->move();
    
    delete pengun3;

    return 0;
}