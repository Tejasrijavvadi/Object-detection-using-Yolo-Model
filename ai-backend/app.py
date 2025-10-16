from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os, uuid
from utils import draw_boxes_and_save, save_json
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# Load pretrained small YOLOv8 model (auto-downloads if not found)
MODEL_PATH = "models/yolov8n.pt"
os.makedirs("models", exist_ok=True)
MODEL = YOLO(MODEL_PATH)

OUTPUT_DIR = "../outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Empty file")

    # Convert bytes → PIL image
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Run inference
    results = MODEL.predict(source=image, device="cpu", imgsz=640)

    res = results[0]
    detections = []
    for *box, conf, cls in res.boxes.data.tolist():
        x1, y1, x2, y2 = map(int, box)
        detections.append({
            "class_id": int(cls),
            "class": MODEL.names[int(cls)],
            "confidence": float(conf),
            "bbox": [x1, y1, x2, y2]
        })

    base = os.path.splitext(file.filename)[0]
    uid = uuid.uuid4().hex[:6]
    json_path = os.path.join(OUTPUT_DIR, f"{base}_{uid}.json")
    img_path = os.path.join(OUTPUT_DIR, f"{base}_{uid}_annotated.jpg")
    save_json(detections, json_path)
    draw_boxes_and_save(contents, detections, img_path)

    return JSONResponse({
        "detections": detections,
        "json_path": json_path,
        "annotated_image_path": img_path
    })

@app.get("/health")
async def health():
    return {"status": "ok"}
