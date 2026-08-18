public class NoodleDish extends FoodItem {
    private String noodleType;
    private String cookingStyle;

    public NoodleDish(String name, double price, String noodleType, String cookingStyle) {
        super(name, price);
        this.noodleType = noodleType;
        this.cookingStyle = cookingStyle;
    }

    @Override
    public void prepare() {
        System.out.println("[ครัวเส้น] กำลังลวก " + noodleType + " และปรุงแบบ " + cookingStyle + " สำหรับ: " + name);
    }

    @Override
    public void displayInfo() {
        System.out.println("[ประเภท: เส้น] " + name + " (" + noodleType + ") | วิธีปรุง: " + cookingStyle + " | ราคา: " + price + " บาท");
    }
}