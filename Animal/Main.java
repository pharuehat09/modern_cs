public class Main {
    public static void main(String[] args) {
        // ใส่ชื่อและอายุ เช่น ร็อคกี้ อายุ 2 ปี, ซีลีน อายุ 4 ปี
        Raccoon myRaccoon = new Raccoon("ร็อคกี้", 2);
        Seal mySeal = new Seal("ซีลีน", 1);

        System.out.println("--- แรคคูน ---");
        myRaccoon.displayInfo();
        myRaccoon.makeSound();
        myRaccoon.washFood();
        myRaccoon.washFood2();
        myRaccoon.washFood3();
        myRaccoon.washFood4();
        myRaccoon.washFood5();
        myRaccoon.washFood6();


        System.out.println("\n--- แมวน้ำ ---");
        mySeal.displayInfo();
        mySeal.makeSound();
        mySeal.swim();
        mySeal.swim2();
        mySeal.swim3();
        mySeal.swim4();
        mySeal.swim5();
        mySeal.swim6();
    }
}