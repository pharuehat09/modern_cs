public class Dog extends Animal {

    public Dog(String name, int age) {
        super(name, age);
    }

    @Override
    public void makeSound() {
        System.out.println(name + " ร้อง: โฮ่งๆ! บ๊อกๆ!");
    }

    // เมธอดเฉพาะตัวของหมา
    public void wagTail() {
        System.out.println(name + " กำลังกระดิกหางอย่างดีใจ");
    }

// เมธอดเฉพาะตัวของหมา
    public void wagTail2() {
        System.out.println(name + " เจอเจ้าของกลับมาจากมหาลัย");
    }
    
    // เมธอดเฉพาะตัวของหมา
    public void wagTail3() {
        System.out.println(name + " เล่นกลับเจ้าของ");
    }

    // เมธอดเฉพาะตัวของหมา
    public void wagTail4() {
        System.out.println(name + " เล่นเสร็จหิว");
    }

    // เมธอดเฉพาะตัวของหมา
    public void wagTail5() {
        System.out.println(name + " เดินไปกินอาหาร");
    }

    // เมธอดเฉพาะตัวของหมา
    public void wagTail6() {
        System.out.println(name + " กินอิ่ม");
    }

    // เมธอดเฉพาะตัวของหมา
    public void wagTail7() {
        System.out.println(name + " นอน");
    }

}