import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# ====== Google API scopes ======
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# ====== 從 Streamlit secrets 讀取 service account ======
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

# ====== 授權 gspread ======
client = gspread.authorize(creds)

# ======（除錯用）顯示目前使用的 service account email ======
st.write("Service Account Email:")
st.write(creds.service_account_email)

# ====== 開啟 Google Sheet（用 key）=====
SHEET_ID = "1PSeyOmGZLsUte982xgB4t-DezSyY3KIFPuhxOoKF5tA"
sheet = client.open_by_key(SHEET_ID).sheet1

# ====== 測試：讀取內容 ======
st.success("成功連上 Google Sheet 🎉")

data = sheet.get_all_records()
st.write(data)
