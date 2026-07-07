public class Seal extends Animal {

    public Seal(String name, int age) {
        super(name, age); // ส่ง name และ age ไปคลาสแม่
    }

    @Override
    public void makeSound() {
        System.out.println(name + " ร้อง: อุ๋งๆ! โฮ่งๆ!");
    }

    public void swim() {
        System.out.println(name + " กำลังว่ายน้ำ");
    }
    
    public void swim2() {
        System.out.println(name + " หาอาหาร");
    }

    public void swim3() {
        System.out.println(name + " หาใด้ปลาตัวเล็กมาสองตัว");
    }

    public void swim4() {
        System.out.println(name + " กินอิ่มแล้ว");
    }

    public void swim5() {
        System.out.println(name + " นอนหลับ");
    }

    public void swim6() {
        System.out.println(name + " ตื่นนอน");
    }
}