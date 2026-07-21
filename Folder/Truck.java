public class Truck extends Vehicle {

    public Truck(String brand) {
        super(brand);
    }

    @Override
    public void startEngine() {
        System.out.println("🚛 รถบรรทุก " + getBrand() + " สตาร์ทเครื่องยนต์: บรึ้มมมม!");
    }

    @Override
    public void drive() {
        System.out.println("🚛 รถบรรทุก " + getBrand() + " กำลังออกจากร้านค้า");
    }

    public void attachTrailer() {
        System.out.println("🚛 รถบรรทุก " + getBrand() + " ต่อพ่วงหลัง บรรทุกได้ 18 ตัน");
    }

    @Override
    public void displayInfo() {
        System.out.println("Truck Brand: " + getBrand());
    }
}