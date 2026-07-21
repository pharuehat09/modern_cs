public class Vehicle {
    private String brand;

    public Vehicle(String brand) {
        this.brand = brand;
    }

    public String getBrand() {
        return brand;
    }

    public void startEngine() {
        System.out.println(brand + " กำลังเดินเครื่อง...");
    }

    // เพิ่มเมธอดสั่งวิ่ง
    public void drive() {
        System.out.println(brand + " กำลังขับเคลื่อนไปข้างหน้า...");
    }

    public void displayInfo() {
        System.out.println("Vehicle Brand: " + brand);
    }
}