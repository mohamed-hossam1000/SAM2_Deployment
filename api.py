from fastapi import FastAPI
import numpy as np
from PIL import Image
import io
import base64
from segment import segment

app = FastAPI()

@app.post("/segment")
async def segment_image(data: dict):
    # Decode base64 image
    image_data = base64.b64decode(data["image"])
    image_pil = Image.open(io.BytesIO(image_data))
    
    # Convert to RGB and numpy array
    if image_pil.mode != 'RGB':
        image_pil = image_pil.convert('RGB')
    image_np = np.array(image_pil)
    
    # Get coordinates
    coordinates_np = np.array(data["coordinates"])
    
    # Segment the image
    segmented_image = segment(image_np, coordinates_np)
    
    # Convert result to base64
    result_pil = Image.fromarray(segmented_image.astype('uint8'))
    buffered = io.BytesIO()
    result_pil.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return {"segmented_image": img_base64}
