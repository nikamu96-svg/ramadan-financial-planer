import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Ramadhan Financial Planner", page_icon="🌙")

st.title("🌙 AI Ramadhan Financial Planner")
st.write("Bantu kamu mengatur keuangan selama bulan Ramadhan dengan lebih bijak.")

# Input Pengguna
income = st.number_input("💰 Pendapatan Bulanan", min_value=0, step=100000)
needs = st.number_input("🛒 Pengeluaran Kebutuhan Pokok (makanan, transport, dsb.)", min_value=0, step=50000)
iftar_budget = st.number_input("🍽️ Budget Bukber / Iftar", min_value=0, step=50000)
ramadhan_goal = st.text_input("🎯 Tujuan Keuangan Ramadhan (contoh: menabung 1 juta, sedekah lebih banyak, dll.)")

if st.button("Analisis Keuangan Ramadhan"):
    
    prompt = f"""
    Kamu adalah AI Financial Planner khusus Ramadhan.
    Analisis data berikut:

    Pendapatan: {income}
    Kebutuhan pokok: {needs}
    Budget iftar: {iftar_budget}
    Tujuan Ramadhan: {ramadhan_goal}

    Buatkan:
    - Analisis kondisi keuangan
    - Rekomendasi pengeluaran ideal Ramadhan
    - Persentase alokasi (kebutuhan, sedekah, tabungan, hiburan)
    - Tips hemat selama Ramadhan
    - Rencana keuangan 30 hari Ramadhan
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("📊 Hasil Analisis AI")
    st.write(response.choices[0].message.content)
