import streamlit as st
import os

st.title("🎓 畢業照網站")

users = {
    "s1121201": "31101",
    "s1120308": "31103",
    "s1121210": "31105",
    "s1120807": "31106",
    "s1120509": "31107",
    "s1121314": "31108",
    "s1120913": "31109",
    "s1120119": "31110",
    "s1120817": "31111",
    "s1120220": "31112",
    "s1120818": "31113",
    "s1120618": "31114",
    "s1121021": "31115",
    "s1120125": "31116",
    "s1121127": "31117",
    "s1120229": "31118",
    "s1121226": "31119",
    "s1120128": "31120",
    "s1120926": "31121",
    "s1121128": "31122",
    "s1121129": "31123",
    "s1121229": "31124",
    "s1121433": "31126",
    "s1120134": "31127",
    "s1121232": "31128",
    "s1120934": "31129",
    "s1121135": "31130",
    "s1120507": "31131"
}

# 初始化登入狀態
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if not st.session_state.logged_in:
    username = st.text_input("帳號（學號）")
    password = st.text_input("密碼", type="password")

    if st.button("登入"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("登入成功")
            st.rerun()
        else:
            st.error("帳號或密碼錯誤")

else:
    username = st.session_state.username
    st.success(f"歡迎你，{username}！")

    photo_folder = f"photos/{username}"

    if os.path.exists(photo_folder):
        photos = sorted(os.listdir(photo_folder))

        if photos:
            for photo in photos:
                st.image(os.path.join(photo_folder, photo))
        else:
            st.info("目前還沒有照片")
    else:
        st.warning("找不到你的照片資料夾")

    if st.button("登出"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

