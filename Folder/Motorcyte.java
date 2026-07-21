public class Motorcyte extends Vehicle {

    public Motorcyte(String brand) {
        super(brand);
    }

    @Override
    public void startEngine() {
        System.out.println("🏍️ รถจักรยานยนต์ " + getBrand() + " สตาร์ทเครื่องยนต์: บรื้นนน!");
    }

    @Override
    public void drive() {
        System.out.println("🏍️ รถจักรยานยนต์ " + getBrand() + " กำลังบิดคันเร่งออกจากบ้าน!");
    }

    public void showWheels() {
        System.out.println("🏍️ รถจักรยานยนต์ " + getBrand() + " มี 2 ล้อ");
    }

    @Override
    public void displayInfo() {
        System.out.println("Motorcycle Brand: " + getBrand());
    }
}