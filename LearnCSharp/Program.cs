namespace LearnCSharp;

class Program 
{
    static void Main(string[] args) 
    {
        Console.WriteLine("Hello, World!");
        int value = 7;
        var value2 = "Hi";
        
        // If statements
        if (value > 5) {
            Console.WriteLine("Value is greater than 5");
        } else {
            Console.WriteLine("Value is 5 or less");
        }

        // For loops
        for (int i = 0; i < 5; i++) {
            Console.WriteLine(i);
        }

        // While loops
        int j = 0;
        while (j < 5) {
            Console.WriteLine(j);
            j++;
        }

        // Methods
        int result = Add(3, 4);

        // Arrays
        int[] numbers = { 1, 2, 3, 4, 5 };

        // Classes
        Person person = new Person("Super Idol", 30);

        // Null conditional operators
        string name = person?.Name ?? "Unknown";
        Console.WriteLine(name);

        // Tuples
        var tuple = ("super idol", 100);
        Console.WriteLine($"Item 1: {tuple.Item1}");

        // Lambdas
        Func<int, int, int> addFunc = (x, y) => x + y;
        int sum = addFunc(5, 10);
        Console.WriteLine(sum);
    }

    public class Person {
        public string Name { get; set; }
        public int Age { get; set; }

        public Person(string name, int age) {
            Name = name;
            Age = age;
        }
    }

    public static int Add(int a, int b) {
        return a + b;
    }
}