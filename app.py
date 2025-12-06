import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Ramadhan Financial Planner", page_icon="🌙")

st.title("🌙 AI Ramadhan Financial Planner")
st.write("Aplikasi cerdas untuk membantu mengatur keuangan selama bulan Ramadhan — dibuat oleh Tuan Muda.")

st.divider()

st.header("🧾 Masukkan Data Keuangan Ramadhan")

income = st.number_input("Masukkan total pemasukan bulan ini (Rp):", min_value=0, step=10000)
food_budget = st.number_input("Budget makanan harian (sahur + buka) (Rp):", min_value=0, step=10000)
infaq = st.number_input("Target infaq per minggu (Rp):", min_value=0, step=10000)
saving_target = st.number_input("Target tabungan selama Ramadhan (Rp):", min_value=0, step=10000)

st.divider()

if st.button("💡 Analisis dan Buatkan Rencana Keuangan"):

    with st.spinner("Sedang menghitung dan menganalisis..."):

        prompt = f"""
        Kamu adalah AI Financial Planner untuk Ramadhan.
        Berdasarkan data berikut:
        - Total pemasukan: {income}
        - Budget makanan harian: {food_budget}
        - Target infaq per minggu: {infaq}
        - Target tabungan Ramadhan: {saving_target}

        Tolong buat:
        1. Ringkasan kondisi keuangan
        2. Rekomendasi alokasi keuangan harian / mingguan
        3. Tips penghematan selama Ramadhan
        4. Saran menu hemat untuk sahur & buka puasa
        5. Rekomendasi target sedekah / infaq
        Buat bahasa Indonesia yang sopan, jelas dan mudah dipahami.
        """

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )

            ai_output = response.choices[0].message["content"]
            st.success("✅ Hasil Analisis dan Rencana Keuangan:")
            st.write(ai_output)

        except Exception as e:
            st.error("⚠️ Terjadi kesalahan saat memproses permintaan. Periksa API key dan model.")
            st.code(str(e))

st.divider()
st.caption("Dibuat oleh Tuan Muda • Powered by Streamlit + Groq AI")
