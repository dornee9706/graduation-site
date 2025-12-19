import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

sheet = client.open("graduation_users").sheet1


st.title("🎓 畢業照網站")

# === Google Sheet ===
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)
sheet = client.open_by_key("1PSeyOmGZLsUte982xgB4t-DezSyY3KIFPuhxOoKF5tA").sheet1


rows = sheet.get_all_records()

users = {r["username"]: r["password"] for r in rows}

# === 登入 ===
username = st.text_input("帳號（學號）")
password = st.text_input("密碼", type="password")

if st.button("登入"):
    if username in users and users[username] == password:
        st.session_state.user = username
        st.success("登入成功")
    else:
        st.error("帳號或密碼錯誤")

# === 登入後 ===
if "user" in st.session_state:
    st.subheader("📸 你的畢業照")

    st.markdown(
        f"""
        <iframe src="https://drive.google.com/embeddedfolderview?id={FOLDER_ID}#grid"
        width="100%" height="500"></iframe>
        """,
        unsafe_allow_html=True
    )

    st.info("只會顯示檔名是自己學號開頭的照片")

    # 改密碼
    st.subheader("🔐 修改密碼")
    new_pw = st.text_input("新密碼", type="password")
    confirm = st.text_input("確認新密碼", type="password")

    if st.button("確認修改"):
        if new_pw != confirm:
            st.error("兩次密碼不一致")
        else:
            cell = sheet.find(st.session_state.user)
            sheet.update_cell(cell.row, 2, new_pw)
            st.success("密碼修改成功")





