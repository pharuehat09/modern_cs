import java.util.ArrayList;
import java.util.List;

public class RestaurantManager {
    private List<FoodItem> menuList = new ArrayList<>();

    public void addMenuItem(FoodItem item) {
        menuList.add(item);
    }

    public void displayAllMenu() {
        System.out.println("=== รายการอาหารทั้งหมดในระบบ ===");
        for (FoodItem item : menuList) {
            item.displayInfo();
        }
        System.out.println();
    }

    public void simulateKitchenPreparation() {
        System.out.println("=== การทำงานของระบบเตรียมอาหาร (Polymorphism) ===");
        for (FoodItem item : menuList) {
            item.prepare();
        }
    }
}