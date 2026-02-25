import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates
import requests
import io
import base64

st.set_page_config(layout="wide")

st.title("🖼️ Image Segmentation App")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Click on the image 👇")

    # Capture click coordinates
    coords = streamlit_image_coordinates(image)

    if coords is not None:
        x, y = coords["x"], coords["y"]
        st.success(f"Clicked at: X={x}, Y={y}")

        # Convert Image to base64 to send as JSON
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Send the request to the backend
        response = requests.post(
            "http://localhost:8000/segment",
            json={
                "image": img_base64,
                "coordinates": [[int(x), int(y)]]
            })

        # Convert response image back from base64
        segmented_image = response.json()["segmented_image"]
        segmented_image = base64.b64decode(segmented_image)
        segmented_image = Image.open(io.BytesIO(segmented_image))

        # Show Segmented Image
        st.subheader("Segmented Image with Selected Point")
        st.image(segmented_image)
