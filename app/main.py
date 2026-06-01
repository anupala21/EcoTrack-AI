import streamlit as st
from prediction import predict_waste
from utils import get_recycling_tip

st.set_page_config(
page_title="EcoTrack AI",
page_icon="♻️",
layout="wide"
)

# Header

st.markdown(
"<h1 style='text-align:center;'>♻️ EcoTrack AI</h1>",
unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align:center;'>Smart Waste Management System</h2>",
    unsafe_allow_html=True
)

st.markdown("""

<div style='text-align:center; font-size:18px;'>
EcoTrack AI uses Artificial Intelligence to identify waste from images,
provide recycling recommendations, and promote sustainable waste disposal
for a cleaner and greener environment.
</div>
""", unsafe_allow_html=True)

st.divider()

# Features Section

st.markdown("### 🚀 Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🤖 AI-based Waste Classification")
    st.success("♻️ Recycling Recommendations")
    st.divider()
    
with col2:
    st.success("🌱 Sustainability Awareness")
    st.success("📊 Future Analytics Dashboard")

    st.divider()
    st.markdown(
        "<h2 style='text-align:left;'>📈 Platform Metrics</h2>",
        unsafe_allow_html=True
    )

left, center, right = st.columns([1,1,1])

with left:
    st.metric("Waste Categories", "5")

with center:
    st.metric("AI Accuracy", "85%")

with right:
    st.metric("Recycling Tips", "Available")

st.divider()

# Upload Section
st.markdown("### 📤 Upload Waste Image")

uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

# Prediction Section

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Waste Image",
        width=400
    )

    waste_type, confidence = predict_waste(uploaded_file)
    tip = get_recycling_tip(waste_type)

    st.markdown("### 📊 Classification Results")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"♻️ Waste Type: {waste_type}")
        st.progress(confidence / 100)
        st.caption(f"Confidence Score: {confidence}%")

    with col2:
        st.info(f"💡 Recycling Tip: {tip}")