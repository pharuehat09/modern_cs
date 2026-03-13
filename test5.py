# 1. ข้อมูลที่ต้องการตรวจสอบ
full_name = "CHANWIT DUANGBUPHA"
student_id = "640123456" # สมมติว่าเป็นสตริงตัวเลข
gpax = 3.25
age = 19

# 2. ฟังก์ชันตรวจสอบและแสดงผล
def check_data_types():
    # ตรวจสอบ FullName เป็น str หรือไม่
    is_name_str = isinstance(full_name, str)
    
    # ตรวจสอบ StudentID เป็น complex (จำนวนเชิงซ้อน) หรือไม่ 
    # (หมายเหตุ: ปกติ ID จะเป็น str หรือ int แต่ในที่นี้เช็คตามโจทย์ครับ)
    is_id_complex = isinstance(student_id, complex)
    
    # ตรวจสอบ Gpax เป็น float หรือไม่
    is_gpax_float = isinstance(gpax, float)
    
    # ตรวจสอบ Age เป็น int หรือไม่
    is_age_int = isinstance(age, int)

    # 3. แสดงผลลัพธ์
    print(f"FullName  : {full_name} => str => {is_name_str}")
    print(f"StudentID : {student_id} => complex => {is_id_complex}")
    print(f"Gpax      : {gpax} => float => {is_gpax_float}")
    print(f"Age       : {age} => int => {is_age_int}")

check_data_types()