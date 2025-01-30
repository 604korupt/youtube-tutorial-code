public class Car extends Vehicle {

    private int mileage;
    private int numberofDoors;

    public Car(String color, int year, int numTires, int mileage, int numberofDoors) {
        super(color, year, numTires);
        this.mileage = mileage;
        this.numberofDoors = numberofDoors;
    }

    public void increaseMileage(int num) {
        mileage += num;
    }

    public void print() {
        super.print();
        System.out.println("Mileage: " + mileage);
        System.out.println("Num of doors: " + numberofDoors);

}