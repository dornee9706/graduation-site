import streamlit as st
import os

st.title("🎓 畢業照網站")

users = {
    "alice": "1234",
    "bob": "5678",
    "clair": "0000"
}

username = st.text_input("帳號")
password = st.text_input("密碼", type="password")

if st.button("登入"):
    if username in users and users[username] == password:
        st.success(f"歡迎你，{username}！")

        photo_folder = f"photos/{username}"

        if os.path.exists(photo_folder):
            photos = os.listdir(photo_folder)

            if photos:
                for photo in photos:
                    st.image(os.path.join(photo_folder, photo))
            else:
                st.info("目前還沒有照片")
        else:
            st.warning("找不到你的照片資料夾")

    else:
        st.error("帳號或密碼錯誤")
