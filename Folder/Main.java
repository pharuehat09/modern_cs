public class Main {

    public static void main(String[] args) {
        // สร้าง Object ของรถแต่ละประเภท
        Car bmw = new Car("BMW");
        Motorcyte Yamaha = new Motorcyte("Yamaha");
        Truck Misumishe = new Truck("Misumishi");

        // --- 🚗 รถยนต์ BMW ---
        System.out.println("=== 🚗 รถยนต์ ===");
        bmw.displayInfo();
        bmw.startEngine();
        bmw.drive();
        bmw.turnLeft();   
        bmw.turnRight();  

        System.out.println();

        // --- 🏍️ รถมอเตอร์ไซค์ Honda ---
        System.out.println("=== 🏍️ รถมอเตอร์ไซค์ ===");
        Yamaha.displayInfo();
        Yamaha.startEngine();
        Yamaha.showWheels(); 
        Yamaha.drive();

        System.out.println();

        // --- 🚛 รถบรรทุก Volvo ---
        System.out.println("=== 🚛 รถบรรทุก ===");
        Misumishe.displayInfo();
        Misumishe.startEngine();
        Misumishe.attachTrailer(); 
        Misumishe.drive();
    }
}