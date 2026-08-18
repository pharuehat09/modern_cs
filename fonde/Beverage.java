public class Beverage extends FoodItem {
    private boolean isCold;

    public Beverage(String name, double price, boolean isCold) {
        super(name, price);
        this.isCold = isCold;
    }

    @Override
    public void prepare() {
        String type = isCold ? "ใส่น้ำแข็งเสิร์ฟเย็น" : "ชงร้อนพร้อมเสิร์ฟ";
        System.out.println("[บาร์น้ำ] กำลังเตรียมเครื่องดื่ม: " + name + " (" + type + ")");
    }

    @Override
    public void displayInfo() {
        String tempStr = isCold ? "เย็น" : "ร้อน";
        System.out.println("[ประเภท: เครื่องดื่ม] " + name + " (" + tempStr + ") | ราคา: " + price + " บาท");
    }
}