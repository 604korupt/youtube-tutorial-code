import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Print Statements
        // Print, then new line
        System.out.println("Hello, World!");
        // Just print without new line
        System.out.print("Hello, World!");

        // declare variables: type varName = value;
        int x = 1;
        double y = 2.5;
        boolean z = true;

        // Java Methods
        int result = multiply(3, 2);

        // Strings + Methods
        String s = "hello";
        int strLength = s.length(); // return 5
        int strIndex = s.indexOf("e"); // return 1
        String strSubString = s.substring(1, 3); // return "el"

        // Math Class
        int absNum = Math.abs(-7);
        double powerNum = Math.pow(2.0, 3.0);
        double sqrtNum = Math.sqrt(25.0);

        // Boolean expressions
        boolean a = false;
        boolean b = true;
        boolean expr = (!a && b) || (a && !b);

        // if statements
        if (x > 1) {
            System.out.println("x is greater than 1");
        } else {
            System.out.println("x is less than or equal to 1");
        }
        
        // For/While loops
        for (int i = 0; i < 3; i++) {
            System.out.println(i);
        }

        int h = 0;
        while (h < 3) {
            System.out.println(h);
            h++;
        }

        // Java Classes
        Vehicle v = new Vehicle("green", 2000, 4);
        v.setColor("red");
        String vColor = v.getColor();
        v.print();
        Vehicle.classMethod();

        //Array
        int[] arr = new int[2];
        arr[0] = 1;
        arr[1] = 2;
        int[] arr1 = {1, 2, 3, 4, 5};

        // Sum of array
        int total = 0;
        for (int i = 0; i < arr1.length; i++) {
            total += arr1[i];
        }

        // ArrayList
        ArrayList<Integer> arrList = new ArrayList<>();
        arrList.add(1);
        arrList.add(2);
        arrList.add(3);
        arrList.set(1, 1);
        arrList.remove(2);
        for (int i = 0; i < arrList.size(); i++) {
            System.out.println(arrList.get(i));
        }

        // 2D Array
        int[][] arr2D = new int[2][2];
        arr2D[0][0] = 1;
        arr2D[0][1] = 2;
        arr2D[1][0] = 3;
        arr2D[1][1] = 4;

        int[][] arr2D1 = {{1, 2, 3}, {4, 5, 6}};
        for (int i = 0; i < arr2D1.length; i++) {
            for (int j = 0; j < arr2D1[i].length; j++) {
                System.out.println(arr2D1[i][j]);
            }
        }

        // Inheritance
        Car c = new Car("Blue", 2010, 4, 10000, 4);
        c.setColor("Yellow");
        c.increaseMileage(10);
        c.print();

        // Recursion
        int recursionMultiply = multiplyRecursion(3, 2);

    }

    public static int multiply(int x, int y) {
        return x * y;
    }

    public static int multiplyRecursion(int x, int y) {
        if (y == 1) {
            return x;
        } else {
            return x + multiplyRecursion(x, y - 1);
        }
    }

}