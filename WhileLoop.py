is_tired = "ไม่"
round_count = 0

print("--- เริ่มการวิ่ง (While Loop) ---")

while is_tired == "ไม่":
    round_count += 1
    print(f"กำลังวิ่งรอบที่ {round_count}")
    
    # ถามความสมัครใจในทุกๆ รอบ
    is_tired = input("เหนื่อยหรือยัง? (ตอบ 'เหนื่อย' เพื่อหยุด / 'ไม่' เพื่อวิ่งต่อ): ")

print(f"สรุปแล้วคุณวิ่งไปทั้งหมด {round_count} รอบ!")