public class Vehicle {

    private String color;
    private int year;
    private int numTires;

    public Vehicle(String color, int year, int numTires) {
        this.color = color;
        this.year = year;
        this.numTires = numTires;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public static void classMethod() {
        System.out.println("This is how to access class methods.");
    }

    public void print() {
        System.out.println("Color: " + color);
        System.out.println("Year: " + year);
        System.out.println("Number of tires: " + numTires);
    }

}