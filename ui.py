import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(layout="centered")

st.title("🖼️ Image Click Coordinate App")

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

        # Create copy of image
        img_with_point = image.copy()
        draw = ImageDraw.Draw(img_with_point)

        # Draw a red circle around clicked point
        r = 10
        draw.ellipse(
            (x - r, y - r, x + r, y + r),
            outline="red",
            width=3
        )

        st.subheader("Image with Selected Point")
        st.image(img_with_point, use_column_width=True)
