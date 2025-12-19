import streamlit as st
from PIL import Image
import hashlib
import cv2
import numpy as np
import io

st.set_page_config(page_title="Deepfake Shield", layout="centered")

st.title("🛡️ Deepfake Shield")
st.subheader("Defending Against Deepfake-Based Information Warfare")

uploaded_file = st.file_uploader(
    "Upload an image for analysis",
    type=["jpg", "png", "jpeg"]
)

def image_hash(img_bytes):
    return hashlib.sha256(img_bytes).hexdigest()

def manipulation_risk(image, img_bytes):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    noise = np.var(gray)
    has_metadata = b'Exif' in img_bytes
    height, width = gray.shape

    indicators = []

    if not has_metadata:
        indicators.append("Metadata stripped (platform re-encoding)")

    if noise > 1500:
        indicators.append("High-frequency artifacts detected")

    if width < 800 or height < 800:
        indicators.append("Low resolution (possible re-share or compression)")

    return indicators


# 🔒 ONLY analyze when an image is uploaded
if uploaded_file:
    img_bytes = uploaded_file.read()

    image = Image.open(io.BytesIO(img_bytes))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    hash_val = image_hash(img_bytes)
    st.write("**Media Integrity Hash:**", hash_val[:16] + "...")

    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    indicators = manipulation_risk(image_cv, img_bytes)

    st.markdown("---")
    st.subheader("🔍 Media Risk Assessment")

    if len(indicators) >= 2:
        st.warning("⚠️ Elevated Risk – Manual Verification Recommended")
        st.write("**Context Indicators:**")
        for i in indicators:
            st.write("•", i)

    elif len(indicators) == 1:
        st.info("ℹ️ Medium Risk – Platform Processing Detected")
        st.write("**Context Indicator:**", indicators[0])

    else:
        st.success("✅ No Obvious Risk Indicators Detected")

    st.markdown("---")
    st.info(
        "Prototype demonstrates contextual media risk indicators. "
        "Final decisions require human or ML verification."
    )

else:
    st.markdown("---")
    st.info("⬆️ Upload an image to begin media risk analysis.")

