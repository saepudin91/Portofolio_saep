import streamlit as st
from PIL import Image
import base64

# Styling
st.set_page_config(page_title="Portofolio Saya", layout="wide")
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
        }
        .main-container {
            background-color: #0f172a;
            color: white;
            padding: 0;
        }
        .header {
            position: relative;
            background-size: cover;
            background-position: center;
            height: 300px;
            border-radius: 0 0 20px 20px;
            margin-bottom: 2rem;
        }
        .header-text {
            position: absolute;
            bottom: 20px;
            left: 40px;
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        }
        .card {
            background-color: #1e293b;
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .badge {
            display: inline-block;
            background-color: #0ea5e9;
            color: white;
            padding: 0.3rem 0.7rem;
            border-radius: 10px;
            font-size: 0.75rem;
            margin-right: 0.5rem;
        }
        .social-links a {
            color: #0ea5e9;
            margin-right: 1rem;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Login Admin Mode
password = st.sidebar.text_input("Masukkan password untuk Admin Mode", type="password")
if password == "admin123":
    st.session_state.admin_mode = True
else:
    st.session_state.admin_mode = False

# Default session state
if "header_image" not in st.session_state:
    st.session_state.header_image = None
if "profile_image" not in st.session_state:
    st.session_state.profile_image = None
if "nama" not in st.session_state:
    st.session_state.nama = "Nama Anda"
if "deskripsi" not in st.session_state:
    st.session_state.deskripsi = "Saya adalah seorang pengembang aplikasi Streamlit yang antusias belajar hal baru."
if "cv_link" not in st.session_state:
    st.session_state.cv_link = ""

# Header Section
st.markdown(f"""
<div class="header" style="background-image: url('{st.session_state.header_image if st.session_state.header_image else 'https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1400&q=80'}');">
  <div class="header-text">{st.session_state.nama}</div>
</div>
""", unsafe_allow_html=True)

# Mode Publik
if not st.session_state.get("admin_mode"):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if st.session_state.profile_image:
        st.image(st.session_state.profile_image, width=150)
    else:
        st.image("https://i.imgur.com/7yUvePI.png", width=150)
    st.markdown(f"*{st.session_state.deskripsi}*")
    st.markdown("""
    <div class="social-links">
        <a href="#">Instagram</a>
        <a href="#">LinkedIn</a>
        <a href="#">GitHub</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Keahlian")
    for skill in st.session_state.get("skills", ["Python", "Streamlit", "Machine Learning"]):
        st.markdown(f"<span class='badge'>{skill}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Pengalaman")
    for exp in st.session_state.get("pengalaman", ["Data Analyst Intern di PT Contoh Data", "Asisten Praktikum Data Science"]):
        st.markdown(f"- {exp}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Proyek Portofolio")
    for proj in st.session_state.get("proyek", ["Aplikasi Prediksi Nilai Siswa Berbasis Streamlit", "Dashboard Interaktif untuk Analisis Penjualan"]):
        st.markdown(f"- {proj}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Hubungi Saya")
    st.markdown("Silakan hubungi saya melalui email: contoh@email.com")
    if st.session_state.get("cv_link"):
        st.markdown(f"""
        <a href="{st.session_state.cv_link}" target="_blank">
            <button style="background-color:#0ea5e9;color:white;padding:10px 20px;border:none;border-radius:10px;margin-top:10px;">
                Unduh CV Saya
            </button>
        </a>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Mode Admin
if st.session_state.get("admin_mode"):
    st.markdown("<div class='badge'>Admin Mode Aktif</div>", unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Update Gambar")
        header_upload = st.file_uploader("Upload Gambar Header", type=["png", "jpg", "jpeg"])
        if header_upload:
            header_bytes = header_upload.read()
            st.session_state.header_image = f"data:image/jpeg;base64,{base64.b64encode(header_bytes).decode()}"

        profile_upload = st.file_uploader("Upload Foto Profil", type=["png", "jpg", "jpeg"])
        if profile_upload:
            profile_bytes = profile_upload.read()
            st.session_state.profile_image = f"data:image/jpeg;base64,{base64.b64encode(profile_bytes).decode()}"

        st.subheader("Informasi Profil")
        st.session_state.nama = st.text_input("Nama", value=st.session_state.nama)
        st.session_state.deskripsi = st.text_area("Deskripsi Singkat", value=st.session_state.deskripsi)

        st.subheader("Link CV")
        st.session_state.cv_link = st.text_input("Masukkan Link CV", value=st.session_state.cv_link)

    for key in ["skills", "pengalaman", "proyek"]:
        if key not in st.session_state:
            st.session_state[key] = []

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Kelola Skills")
    new_skill = st.text_input("Tambah Skill", key="new_skill")
    if st.button("Tambah Skill"):
        if new_skill:
            st.session_state.skills.append(new_skill)
    for i, skill in enumerate(st.session_state.skills):
        col1, col2 = st.columns([6, 1])
        col1.write(f"- {skill}")
        if col2.button("❌", key=f"del_skill_{i}"):
            st.session_state.skills.pop(i)
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Kelola Pengalaman")
    new_exp = st.text_input("Tambah Pengalaman", key="new_exp")
    if st.button("Tambah Pengalaman"):
        if new_exp:
            st.session_state.pengalaman.append(new_exp)
    for i, exp in enumerate(st.session_state.pengalaman):
        col1, col2 = st.columns([6, 1])
        col1.write(f"- {exp}")
        if col2.button("❌", key=f"del_exp_{i}"):
            st.session_state.pengalaman.pop(i)
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Kelola Proyek")
    new_proj = st.text_input("Tambah Proyek", key="new_proj")
    if st.button("Tambah Proyek"):
        if new_proj:
            st.session_state.proyek.append(new_proj)
    for i, proj in enumerate(st.session_state.proyek):
        col1, col2 = st.columns([6, 1])
        col1.write(f"- {proj}")
        if col2.button("❌", key=f"del_proj_{i}"):
            st.session_state.proyek.pop(i)
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="border: 1px solid #0ea5e9;">
<center><small>© 2025 Dibuat dengan Streamlit</small></center>
""", unsafe_allow_html=True)
