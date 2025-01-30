package main

import "fmt"

func main() {
    // Variables
    var a int = 1
    shortHand := 2

    message, randomInt, isIdol := "hi", 25, true
    fmt.Println(message)
    fmt.Println(randomInt)
    fmt.Println(isIdol)
    fmt.Println(shortHand)

    // If statements
    if a == 1 {
        fmt.Println("a is 1")
    } else {
        fmt.Println("a is not 1")
    }

    // For loops
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }

    // Functions
    fmt.Println(add(1, 2))

    // Arrays
    var arr[3] int
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3

    arr2 := [3]int{1, 2, 3}
    fmt.Println(arr2)

    // Maps
    superMap := map[string]int{"super":1, "idol":2}
    superMap["smile"] = 3
    fmt.Println(superMap)

    // Structs
    type Person struct {
        name string
        age int
    }

    var p Person
    p.name = "Super Idol"
    p.age = 25

    // Pointers
    var b int = 1
    var c *int = &b
    fmt.Println(c)

}

// func name(parameters) return type
func add(a int, b int) int {
    return a + b
}