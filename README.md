# 🖼️ Image Segmentation App

A web app that lets you click on any image to instantly segment and extract the object at that location, powered by Meta's SAM2 (Segment Anything Model 2).

## How It Works

1. Upload an image
2. Click on the object you want to segment
3. The app isolates the object against a white background

## Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Model:** SAM2 (`sam2.1_hiera_large`)

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Download the SAM2 checkpoint

Download `sam2.1_hiera_large.pt` from the [SAM2 releases](https://github.com/facebookresearch/segment-anything-2) and place it in a `checkpoints/` folder in the project root.

### 3. Start the backend

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

### 4. Start the frontend

```bash
streamlit run ui.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Project Structure

```
├── api.py            # FastAPI backend
├── segment.py        # SAM2 segmentation logic
├── ui.py             # Streamlit frontend
├── requirements.txt
└── checkpoints/
    └── sam2.1_hiera_large.pt
```

## Notes

- The model runs on CPU by default. For faster inference, change `device="cpu"` to `device="cuda"` in `segment.py` if you have a GPU.
