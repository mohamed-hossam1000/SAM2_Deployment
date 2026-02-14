from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor
import numpy as np


checkpoint = "./checkpoints/sam2.1_hiera_large.pt"
model_cfg = "configs/sam2.1/sam2.1_hiera_l.yaml"
predictor = SAM2ImagePredictor(build_sam2(model_cfg, checkpoint, device="cpu"))

def segment(image, coordinates):
    predictor.set_image(image)
    masks, scores, logits = predictor.predict(
        point_coords=coordinates,
        point_labels=np.array([1]),
        multimask_output=False
    )
    
    masked_image = image.copy()
    masked_image[masks[0] == 0] = [255, 255, 255]  

    return masked_image