# รับจำนวนรอบจากผู้ใช้
total_rounds = int(input("คุณต้องการวิ่งกี่รอบ? : "))

print("--- เริ่มการวิ่ง (For Loop) ---")

for round_count in range(1, total_rounds + 1):
    print(f"กำลังวิ่งรอบที่ {round_count}")

print("เย้! วิ่งครบตามเป้าหมายแล้ว")