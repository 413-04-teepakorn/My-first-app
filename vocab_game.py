st.title("🍎 เกมเติมคำศัพท์ภาษาอังกฤษ (4 ข้อ)")

# จุดที่ 1: กำหนดค่าเริ่มต้นใน session_state (ans1_val ถึง ans4_val)
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# จุดที่ 2: เพิ่มการเคลียร์ค่าเมื่อกดเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()


# Dialog สรุปผลการเล่นเกม (รับค่า ans1, ans2, ans3, ans4)
@st.dialog("สรุปผลคะแนน")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    # จุดที่ 3: จัดการข้อความ input
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1 และ 2
    if u_ans1 == "apple":
        st.success("ถูกต้อง ข้อ 1: apple")
        score += 1
    else:
        st.error("❌ ข้อ 1: ไม่ถูกต้อง (เฉลย: apple)")

    if u_ans2 == "banana":
        st.success("ถูกต้อง ข้อ 2: banana")
        score += 1
    else:
        st.error("❌ ข้อ 2: ไม่ถูกต้อง (เฉลย: banana)")

    # จุดที่ 4: ตรวจข้อ 3 และข้อ 4
    if u_ans3 == "Pineapple":
        st.success("ถูกต้อง ข้อ 3: Pineaplle")
        score += 1
    else:
        st.error("❌ ข้อ 3: ไม่ถูกต้อง (เฉลย: Pineapple)")

    if u_ans4 == "dog":
        st.success("ถูกต้อง ข้อ 4: Coconut")
        score += 1
    else:
        st.error("❌ ข้อ 4: ไม่ถูกต้อง (เฉลย: Coconut)")

    # จุดที่ 5: เพิ่มคะแนนเต็ม score == 4
    st.write(f"### คุณได้คะแนนทั้งหมด {score} / 4 คะแนน")
    if score == 4:
        st.balloons()
        st.success("🎉 ยินดีด้วย! คุณตอบถูกครบทุกข้อ!")


# --- ส่วนอินเทอร์เฟซรับคำตอบ ---

# ข้อ 1 & 2
ans1 = st.text_input("1. 🍎 คำศัพท์ภาษาอังกฤษของ 'แอปเปิ้ล'", value=st.session_state.ans1_val)
ans2 = st.text_input("2. 🍌 คำศัพท์ภาษาอังกฤษของ 'กล้วย'", value=st.session_state.ans2_val)

# จุดที่ 6: เพิ่มช่องรับคำตอบ ans3 และ ans4
ans3 = st.text_input("3. 🐱 คำศัพท์ภาษาอังกฤษของ 'แมว'", value=st.session_state.ans3_val)
ans4 = st.text_input("4. 🐶 คำศัพท์ภาษาอังกฤษของ 'สุนัข'", value=st.session_state.ans4_val)

# จุดที่ 7: อัปเดตค่าล่าสุดเข้าตัวแปร session_state
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# ปุ่มส่งคำตอบ
if st.button("ส่งคำตอบ"):
    # จุดที่ 8: แสดง Dialog ผลลัพธ์โดยส่งค่า ans1, ans2, ans3, ans4
    show_result_dialog(ans1, ans2, ans3, ans4)
