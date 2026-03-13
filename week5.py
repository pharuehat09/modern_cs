def get_grade_and_point(score):
    # ตรรกะใหม่: ถ้าไม่ผ่าน (ต่ำกว่า 50) เท่ากับ E
    if score >= 80:
        return "A", 4.0
    elif score >= 70:
        return "B", 3.0
    elif score >= 60:
        return "C", 2.0
    elif score >= 50:
        return "D", 1.0
    else:
        return "E", 0.0  # เปลี่ยนจาก F เป็น E ตามโจทย์

# ส่วนการรับข้อมูลและประมวลผล
results = []
print("=== ระบบตัดเกรด (เกณฑ์ E = ไม่ผ่าน) ===")

while True:
    subject = input("\nระบุชื่อวิชา (หรือพิมพ์ 'e' เพื่อจบ): ")
    if subject.lower() == 'e':
        break
        
    try:
        score_val = float(input(f"กรอกคะแนนวิชา {subject} (0-100): "))
        
        if 0 <= score_val <= 100:
            grade_letter, grade_point = get_grade_and_point(score_val)
            results.append({"name": subject, "score": score_val, "grade": grade_letter})
            print(f"-> ผลการเรียน: {grade_letter}")
        else:
            print("! ข้อผิดพลาด: คะแนนต้องอยู่ในช่วง 0-100")
            
    except ValueError:
        print("! ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลข")

# แสดงตารางสรุป
print("\n" + "="*40)
print(f"{'วิชา':<15} | {'คะแนน':<10} | {'เกรด':<5}")
print("-" * 40)
for item in results:
    print(f"{item['name']:<15} | {item['score']:<10.1f} | {item['grade']:<5}")
print("="*40)