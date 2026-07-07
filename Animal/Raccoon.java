public class Raccoon extends Animal {

    public Raccoon(String name, int age) {
        super(name, age); // ส่ง name และ age ไปคลาสแม่
    }

    @Override
    public void makeSound() {
        System.out.println(name + " ร้อง: จี๊ดๆ แกร๊กๆ!");
    }

    public void washFood() {
        System.out.println(name + " กำลังหาอาหาร");
    }

    public void washFood2() {
        System.out.println(name + " กินอาหาร");
    }

    public void washFood3() {
        System.out.println(name + " กินเสร็จหาที่นอน");
    }

public void washFood4() {
        System.out.println(name + " นอน");
    }

    public void washFood5() {
        System.out.println(name + " ตื่นนอน");
    }
    
    public void washFood6() {
        System.out.println(name + " ทำความสะอาดตัว");
    }

}