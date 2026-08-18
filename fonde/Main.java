public class Main {
    public static void main(String[] args) {
        RestaurantManager manager = new RestaurantManager();

        // เพิ่มข้อมูลแยกตามประเภท
        manager.addMenuItem(new RiceDish("ข้าวผัดกุ้ง", 1, "ผัด"));
        manager.addMenuItem(new NoodleDish("ก๋วยเตี๋ยวต้มยำ", 2, "เส้นเล็ก", "ต้ม"));
        manager.addMenuItem(new Beverage("ชาไทย", 1, true));

        // แสดงผล
        manager.displayAllMenu();
        manager.simulateKitchenPreparation();
    }
}