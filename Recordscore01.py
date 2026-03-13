import tkinter as tk
from tkinter import messagebox

def start_app():
    root = tk.Tk()
    root.title("Scoreboard System")
    root.geometry("400x500")

    # ตัวแปรเก็บข้อมูล
    teams = {}
    MAX_TEAMS = 4
    current_round = [1] # ใช้ list เพื่อให้เปลี่ยนแปลงค่าในฟังก์ชันย่อยได้

    # ส่วนบน: ลงทะเบียน
    frame_reg = tk.LabelFrame(root, text=" 1. ลงทะเบียน (4 ทีม) ")
    frame_reg.pack(pady=10, padx=10, fill="x")

    ent_name = tk.Entry(frame_reg)
    ent_name.pack(side="left", padx=5, pady=5, expand=True, fill="x")

    def add_team():
        name = ent_name.get().strip()
        if name and name not in teams and len(teams) < MAX_TEAMS:
            teams[name] = 0
            lbl_status.config(text=f"ลงทะเบียนแล้ว: {list(teams.keys())}")
            ent_name.delete(0, tk.END)
            if len(teams) == MAX_TEAMS:
                btn_reg.config(state="disabled")
                enable_scoring()
        elif name in teams:
            messagebox.showwarning("เตือน", "ชื่อทีมซ้ำ!")

    btn_reg = tk.Button(frame_reg, text="เพิ่มทีม", command=add_team)
    btn_reg.pack(side="right", padx=5)

    lbl_status = tk.Label(root, text="กรุณาเพิ่มให้ครบ 4 ทีม", fg="blue")
    lbl_status.pack()

    # ส่วนกลาง: บันทึกคะแนน
    frame_score = tk.LabelFrame(root, text=" 2. บันทึกคะแนน (6 รอบ) ")
    frame_score.pack(pady=10, padx=10, fill="both", expand=True)

    score_entries = {}

    def enable_scoring():
        lbl_round.config(text=f"🚩 รอบที่: {current_round[0]} / 6")
        for name in teams:
            f = tk.Frame(frame_score)
            f.pack(fill="x", pady=2)
            tk.Label(f, text=f"{name}:", width=12).pack(side="left")
            e = tk.Entry(f)
            e.pack(side="right", expand=True, fill="x", padx=5)
            e.insert(0, "0")
            score_entries[name] = e
        btn_submit.config(state="normal")

    lbl_round = tk.Label(frame_score, text="รอลงทะเบียนครบ...", font=("Arial", 10, "bold"))
    lbl_round.pack(pady=5)

    def submit():
        try:
            # ตรวจสอบและบวกคะแนน
            for name, entry in score_entries.items():
                pts = int(entry.get())
                if 0 <= pts <= 10:
                    teams[name] += pts
                    entry.delete(0, tk.END)
                    entry.insert(0, "0")
                else:
                    messagebox.showerror("ผิดพลาด", "ใส่ได้แค่ 0-10 แต้ม")
                    return

            if current_round[0] < 6:
                current_round[0] += 1
                lbl_round.config(text=f"🚩 รอบที่: {current_round[0]} / 6")
                update_display()
            else:
                final_result()
        except:
            messagebox.showerror("ผิดพลาด", "กรุณาใส่เฉพาะตัวเลข")

    btn_submit = tk.Button(frame_score, text="บันทึกคะแนน", command=submit, state="disabled", bg="green", fg="white")
    btn_submit.pack(pady=10)

    # ส่วนล่าง: แสดงผลสรุป
    lbl_display = tk.Label(root, text="", font=("Courier", 10), justify="left")
    lbl_display.pack(pady=10)

    def update_display():
        sorted_res = sorted(teams.items(), key=lambda x: x[1], reverse=True)
        txt = "อันดับปัจจุบัน:\n"
        for i, (n, s) in enumerate(sorted_res, 1):
            txt += f"{i}. {n[:10]:<10} | {s} แต้ม\n"
        lbl_display.config(text=txt)

    def final_result():
        sorted_res = sorted(teams.items(), key=lambda x: x[1], reverse=True)
        winner = sorted_res[0][0]
        messagebox.showinfo("จบการแข่งขัน", f"ผู้ชนะคือทีม: {winner}\nคะแนน: {sorted_res[0][1]}")
        root.destroy()

    root.mainloop()

if __name__ == "__main__":
    start_app()