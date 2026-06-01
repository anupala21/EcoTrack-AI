import streamlit as st

st.set_page_config(
    page_title="EcoTrack AI",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ EcoTrack AI")
st.subheader("Smart Waste Management System")

st.write("""
Welcome to EcoTrack AI.

This platform helps classify waste and promotes
sustainable recycling practices.
""")

uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Waste Image")

    st.success("Image uploaded successfully!")

    st.info("AI prediction module coming soon...")
