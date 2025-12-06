import streamlit as st
from groq import Groq
import os

# Inisialisasi client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Konfigurasi halaman
st.set_page_config(page_title="AI Ramadhan Financial Planner", page_icon="🌙")

st.title("🌙 AI Ramadhan Financial Planner")
st.write("Aplikasi untuk membantu mengatur keuangan selama Ramadhan — dibuat oleh Tuan Muda.")

st.divider()

# Input data keuangan
st.header("🧾 Masukkan Data Keuangan Ramadhan")

income = st.number_input("Pemasukan bulan ini (Rp):", min_value=0, step=10000)
food_budget = st.number_input("Budget makan harian (Rp):", min_value=0, step=10000)
infaq = st.number_input("Target infaq per minggu (Rp):", min_value=0, step=10000)
saving_target = st.number_input("Target tabungan Ramadhan (Rp):", min_value=0, step=10000)

st.divider()

# Tombol proses
if st.button("💡 Analisis & Buatkan Rencana"):

    with st.spinner("AI sedang menghitung dan menganalisis..."):

        prompt = f"""
        Buatkan analisis rencana keuangan Ramadhan berdasarkan data berikut:

        - Pemasukan bulanan: Rp {income}
        - Budget makanan harian: Rp {food_budget}
        - Target infaq per minggu: Rp {infaq}
        - Target tabungan: Rp {saving_target}

        Buat output:
        1. Ringkasan kondisi keuangan
        2. Rekomendasi alokasi harian & mingguan
        3. Tips penghematan Ramadhan
        4. Contoh menu sahur & buka hemat
        5. Saran infaq/sedekah mingguan

        Gunakan bahasa Indonesia yang sopan, jelas, dan rapi.
        """

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # FIX PENTING: Ambil output dengan benar
            ai_output = response.choices[0].message.content

            st.success("✅ Hasil Analisis Keuangan Ramadhan Anda:")
            st.write(ai_output)

        except Exception as e:
            st.error("⚠️ Terjadi kesalahan. Periksa API key dan model.")
            st.code(str(e))

st.divider()
st.caption("Dibuat oleh Tuan Muda • Powered by Groq AI + Streamlit")
