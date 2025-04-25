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
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        .badge {
            display: inline-block;
            background-color: #0ea5e9;
            color: white;
            padding: 0.3rem 0.7rem;
            border-radius: 10px;
            font-size: 0.75rem;
            margin: 0.3rem 0.3rem 0 0;
        }
        .social-links a {
            color: #0ea5e9;
            margin-right: 1rem;
            text-decoration: none;
            font-weight: bold;
        }
        @media screen and (max-width: 768px) {
            .header {
                height: 200px !important;
            }
            .header-text {
                font-size: 1.5rem !important;
                left: 20px !important;
                bottom: 15px !important;
            }
            .card {
                padding: 1rem !important;
            }
            .stImage img {
                width: 100% !important;
                height: auto !important;
                border-radius: 12px;
            }
            .stButton button {
                font-size: 0.85rem !important;
            }
            .social-links a {
                display: block;
                margin-bottom: 0.5rem;
            }
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
for key in ["skills", "pengalaman", "proyek"]:
    if key not in st.session_state:
        st.session_state[key] = []

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
        st.image(st.session_state.profile_image, use_column_width=True)
    else:
        st.image("https://i.imgur.com/7yUvePI.png", use_column_width=True)
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
    for skill in st.session_state.get("skills", []):
        st.markdown(f"<span class='badge'>{skill}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Pengalaman")
    for exp in st.session_state.get("pengalaman", []):
        st.markdown(f"- {exp}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Proyek Portofolio")
    for proj in st.session_state.get("proyek", []):
        st.markdown(f"- {proj}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Hubungi Saya")
    st.markdown("Silakan hubungi saya melalui email: contoh@email.com")
    if st.session_state.get("cv_link"):
        st.markdown(f"""
        <a href="{st.session_state.cv_link}" download="CV_{st.session_state.nama}.pdf" target="_blank">
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

        st.subheader("Link / Upload CV")
        st.session_state.cv_link = st.text_input("Atau Masukkan Link CV", value=st.session_state.cv_link)
        cv_upload = st.file_uploader("Atau Upload File CV (PDF)", type=["pdf"])
        if cv_upload:
            cv_bytes = cv_upload.read()
            b64_cv = base64.b64encode(cv_bytes).decode()
            st.session_state.cv_link = f"data:application/pdf;base64,{b64_cv}"
            st.success("CV berhasil diunggah dan siap diunduh!")

    # Kelola Skills
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Kelola Skills")
    new_skill = st.text_input("Tambah Skill", key="new_skill")
    if st.button("Tambah Skill"):
        if new_skill:
            st.session_state.skills.append(new_skill)
            st.rerun()
    for i, skill in enumerate(st.session_state.skills):
        col1, col2 = st.columns([6, 1])
        col1.write(f"- {skill}")
        if col2.button("❌", key=f"del_skill_{i}"):
            st.session_state.skills.pop(i)
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # Kelola Pengalaman
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Kelola Pengalaman")
    new_exp = st.text_input("Tambah Pengalaman", key="new_exp")
    if st.button("Tambah Pengalaman"):
        if new_exp:
            st.session_state.pengalaman.append(new_exp)
            st.rerun()
    for i, exp in enumerate(st.session_state.pengalaman):
        col1, col2 = st.columns([6, 1])
        col1.write(f"- {exp}")
        if col2.button("❌", key=f"del_exp_{i}"):
            st.session_state.pengalaman.pop(i)
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # Kelola Proyek
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Kelola Proyek")
    new_proj = st.text_input("Tambah Proyek", key="new_proj")
    if st.button("Tambah Proyek"):
        if new_proj:
            st.session_state.proyek.append(new_proj)
            st.rerun()
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

# Auto scroll to top
st.markdown("""
<script>
    window.scrollTo(0, 0);
</script>
""", unsafe_allow_html=True)
