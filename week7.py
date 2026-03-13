class Student:
    def __init__(self, student_id, name, nickname, phone, email):
        self.student_id = student_id
        self.name = name
        self.nickname = nickname
        self.phone = phone
        self.email = email

    def display_info(self):
        print(f"รหัสนักศึกษา: {self.student_id}")
        print(f"ชื่อ-นามสกุล: {self.name} ({self.nickname})") # เพิ่มชื่อเล่นในวงเล็บ
        print(f"เบอร์โทรศัพท์: {self.phone}") # ข้อมูลใหม่
        print(f"อีเมล: {self.email}")      # ข้อมูลใหม่
        print("-" * 30)

# ส่วนของการรับข้อมูล
students_list = []

def add_student():
    print("\n--- กรอกข้อมูลนักศึกษาใหม่ ---")
    s_id = input("รหัสนักศึกษา: ")
    name = input("ชื่อ-นามสกุล: ")
    nick = input("ชื่อเล่น: ")  # 1. เพิ่มชื่อเล่น
    tel = input("เบอร์โทร: ")  # 2. เพิ่มเบอร์โทร
    mail = input("อีเมล: ")    # 3. เพิ่มอีเมล
    
    new_student = Student(s_id, name, nick, tel, mail)
    students_list.append(new_student)
    print("บันทึกข้อมูลสำเร็จ!\n")

# ทดสอบการใช้งาน
add_student()
for s in students_list:
    s.display_info()