// Variables
let num: number = 10;

// Any type
let anyVar: any = "Can be anything";
let anyVar2: any = 10;
let anyVar3: any = true;

// If statements
if (num > 0) {
    console.log("Positive");
} else {
    console.log("Non-positive");
}

// For loops
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// While loops
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// Functions 
// function name(parameters): return type
function add(a: number, b: number): number {
    return a + b;
}

console.log(add(1, 2));

// Arrays
let arr: number[] = [1, 2, 3];
console.log(arr[0]);

// Objects 
type Point = { x: number, y: number };
let point: Point = { x: 1, y: 2 }; 

// Classes
class Idol {
    private name: string;

    public constructor(name: string) {
        this.name = name;
    }

    public getName(): string {
        return this.name;
    }
}

let idol = new Idol("Super Idol");
console.log(idol.getName());

// Interfaces
interface Person {
    name: string;
    age: number;
}

let person: Person = { name: "Alice", age: 30 };

// Generics
function createPair<S, T>(v1: S, v2: T): [S, T] {
    return [v1, v2];
}

console.log(createPair<string, number>('hello', 42));

// Union types
function printId(id: number | string) {
    console.log(id);
}

printId(1);
printId('abc');