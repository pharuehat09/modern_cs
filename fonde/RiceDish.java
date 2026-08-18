public class RiceDish extends FoodItem {
    private String cookingMethod;

    public RiceDish(String name, double price, String cookingMethod) {
        super(name, price);
        this.cookingMethod = cookingMethod;
    }

    @Override
    public void prepare() {
        System.out.println("[ครัวข้าว] กำลัง " + cookingMethod + " เมนู: " + name);
    }

    @Override
    public void displayInfo() {
        System.out.println("[ประเภท: ข้าว] " + name + " | วิธีปรุง: " + cookingMethod + " | ราคา: " + price + " บาท");
    }
}