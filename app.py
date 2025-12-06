import streamlit as st
from groq import Groq
import os

# ========================
# 1. KONFIGURASI API GROQ
# ========================
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ========================
# 2. TAMPILAN HEADER
# ========================
st.set_page_config(page_title="AI Ramadhan Financial Planner", page_icon="🌙")

st.title("🌙 AI Ramadhan Financial Planner")
st.write("Aplikasi cerdas untuk membantu mengatur keuangan selama bulan Ramadhan – dibuat oleh Tuan Muda.")

st.divider()

# ========================
# 3. INPUT USER
# ========================
st.header("🧾 Masukkan Data Keuangan Ramadhan")

income = st.number_input("Masukkan total pemasukan bulan ini (Rp):", min_value=0)
food_budget = st.number_input("Budget makanan harian (sahur + buka):", min_value=0)
infaq = st.number_input("Target infaq per minggu:", min_value=0)
saving_target = st.number_input("Target tabungan selama Ramadhan:", min_value=0)

st.divider()

# ========================
# 4. PROSES DENGAN AI GROQ
# ========================
if st.button("💡 Analisis dan Buatkan Rencana Keuangan"):

    with st.spinner("Sedang menghitung dan menganalisis..."):

        prompt = f"""
        Buatkan analisis dan rekomendasi perencanaan keuangan selama bulan Ramadhan berdasarkan data berikut:

        - Total pemasukan: {income}
        - Budget makanan harian: {food_budget}
        - Target infaq per minggu: {infaq}
        - Target tabungan Ramadhan: {saving_target}

        Berikan output:
        1. Ringkasan pola keuangan
        2. Rekomendasi alokasi keuangan harian & mingguan
        3. Tips penghematan selama Ramadhan
        4. Saran menu hemat untuk sahur & buka
        5. Rekomendasi target ibadah (infaq, sedekah)
        Buat bahasa yang sopan, jelas, dan mudah dipahami.
        """

        # ========================
        # Pemanggilan API Groq
        # ========================
        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            ai_output = response.choices[0].message["content"]

            st.success("Berhasil! Berikut hasil analisis keuangan Ramadhan Anda:")
            st.write(ai_output)

        except Exception as e:
            st.error("Terjadi kesalahan saat memproses permintaan. Pastikan API key valid.")
            st.code(str(e))

st.divider()

# ========================
# 5. FOOTER
# ========================
st.caption("Dibuat oleh Tuan Muda • Powered by Streamlit + Groq AI")
