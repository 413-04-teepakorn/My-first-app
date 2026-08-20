import time
import streamlit as st

st.title("🍎 เกมเติมคำศัพท์ภาษาอังกฤษ")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""


# ฟังก์ชันรีเซ็ตเพื่อเริ่มเล่นใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์คำตอบข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์คำตอบข้อ 2
    st.session_state.start = time.time()  # ตั้งเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# สรุปผลการเล่นเกม (Dialog)
@st.dialog("สรุปผลคะแนน")
def show_result_dialog(ans1, ans2):
    st.balloon()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("ถูกต้อง 1: แอปเปิ้ล")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ไม่ถูกต้อง (คำตอบคือ 'apple')")
