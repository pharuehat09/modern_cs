public class Animal {
    protected String name;
    protected int age; // เพิ่มตัวแปรอายุ

    // ปรับ Constructor ให้รับค่าอายุด้วย
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void makeSound() {
        System.out.println("สัตว์ส่งเสียงร้องทั่วไป");
    }

    public void displayInfo() {
        System.out.println("ชื่อสัตว์: " + name);
        System.out.println("อายุ: " + age + " ปี"); // แสดงอายุ
    }
}