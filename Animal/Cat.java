public class Cat extends Animal {

    public Cat(String name, int age) {
        super(name, age);
    }

    @Override
    public void makeSound() {
        System.out.println(name + " ร้อง: เหมียวๆ~ ม้าววว!");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture() {
        System.out.println(name + " กำลังฝนเล็บกับโซฟา");
    }
    
    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture2() {
        System.out.println(name + " เดินไป");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture3() {
        System.out.println(name + " หาของเล่น");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture4() {
        System.out.println(name + " เล่นจนเบื่อละ");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture5() {
        System.out.println(name + " เดินไปหาของกิน");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture6() {
        System.out.println(name + " ใด้ของกินแล้ว");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture7() {
        System.out.println(name + " กินอิ่ม");
    }

    // เมธอดเฉพาะตัวของแมว
    public void scratchFurniture8() {
        System.out.println(name + " นอน");
    }

}