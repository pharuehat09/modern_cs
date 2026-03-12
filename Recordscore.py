def scoreboard_system():
    scores = {}
    teams_list = []
    MAX_TEAMS = 4
    MAX_ROUNDS = 6
    MAX_POINTS = 10
    
    print(f"=== 🏆 ระบบจัดการคะแนน (4 ทีม | 6 รอบ) 🏆 ===")
    print(f"** กติกา: ให้ได้ครั้งละไม่เกิน {MAX_POINTS} แต้ม **")
    print("กด [h] - เริ่มบันทึกคะแนน | กด [q] - ออกจากระบบ")

    while True:
        main_choice = input("\nเมนูหลัก (h/q): ").lower().strip()

        if main_choice == 'q':
            print("ปิดระบบ...")
            break
        
        elif main_choice == 'h':
            # 1. ลงทะเบียนทีม (เฉพาะครั้งแรก)
            if not teams_list:
                print(f"\n--- 📋 ลงทะเบียนทีมให้ครบ {MAX_TEAMS} ทีมก่อนเริ่ม ---")
                while len(teams_list) < MAX_TEAMS:
                    name = input(f"ระบุชื่อทีมที่ {len(teams_list)+1}: ").strip()
                    if name and name not in teams_list:
                        teams_list.append(name)
                        scores[name] = 0
                    else:
                        print("⚠️ ชื่อซ้ำหรือว่างเปล่า กรุณากรอกใหม่")

            # 2. เริ่มบันทึกคะแนนทีละรอบ
            for round_num in range(1, MAX_ROUNDS + 1):
                print(f"\n" + "="*40)
                print(f"🚩 รอบที่ {round_num} / {MAX_ROUNDS}")
                print("="*40)
                
                for team in teams_list:
                    while True:
                        try:
                            print(f"\n>> ทีม: {team} (คะแนนเดิม: {scores[team]})")
                            points = int(input(f"   บวกคะแนนรอบนี้ (0-{MAX_POINTS}): "))
                            
                            if 0 <= points <= MAX_POINTS:
                                old_score = scores[team]
                                scores[team] += points
                                
                                # สรุปคะแนนล่าสุดของทีมนี้
                                print(f"   ✅ บันทึก: {old_score} + {points} = {scores[team]}")
                                break
                            else:
                                print(f"   ❌ ปฏิเสธ: ต้องอยู่ระหว่าง 0-{MAX_POINTS} เท่านั้น")
                        except ValueError:
                            print("   ⚠️ กรุณากรอกตัวเลขเท่านั้น")

                # สรุปตารางคะแนนเมื่อจบรอบ
                print(f"\n📊 ตารางคะแนนหลังจบรอบที่ {round_num}:")
                sorted_temp = sorted(scores.items(), key=lambda x: x[1], reverse=True)
                for rank, (name, score) in enumerate(sorted_temp, 1):
                    print(f"อันดับ {rank}. {name:15} | รวม {score} แต้ม")
                
                if round_num < MAX_ROUNDS:
                    cont = input("\nกด Enter เพื่อต่อรอบถัดไป หรือพิมพ์ 'q' เพื่อหยุดแค่นี้: ").lower()
                    if cont == 'q': break
            
            # เมื่อครบ 6 รอบ จะบังคับสรุปผลและออกไปที่เมนูหลัก
            print("\n✨ ครบกำหนด 6 รอบเรียบร้อยแล้ว!")
            break 
        
        else:
            print("❌ คำสั่งไม่ถูกต้อง กรุณาใช้ h หรือ q")

    # 3. สรุปผลสุดท้าย (Final Result)
    if scores:
        print("\n" + "═"*45)
        print("🎊 สรุปผลการแข่งขันรอบสุดท้าย 🎊")
        print("═"*45)
        final_rank = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for i, (name, score) in enumerate(final_rank, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "
            print(f"{medal} อันดับ {i}: {name:15} | คะแนนรวม: {score}")
        print(f"\n🎉 ยินดีกับทีม {final_rank[0][0]}!")

if __name__ == "__main__":
    scoreboard_system()