public class Car extends Vehicle {

    public Car(String brand) {
        super(brand);
    }

    @Override
    public void startEngine() {
        System.out.println("🚗 รถยนต์ " + getBrand() + " สตาร์ทเครื่องยนต์: บรื้นๆ!");
    }

    @Override
    public void drive() {
        System.out.println("🚗 รถยนต์ " + getBrand() + " กำลังเร่งด้วยความเร็วต่ำออกจากบ้าน! ");
    }

    public void turnLeft() {
        System.out.println("🚗 รถยนต์ " + getBrand() + " เลี้ยวซ้าย (Turn Left)");
    }

    public void turnRight() {
        System.out.println("🚗 รถยนต์ " + getBrand() + " เลี้ยวขวา (Turn Right)");
    }

    @Override
    public void displayInfo() {
        System.out.println("Car Brand: " + getBrand());
    }
}