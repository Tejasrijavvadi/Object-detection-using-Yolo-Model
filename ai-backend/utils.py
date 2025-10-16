import io, json, os
from PIL import Image, ImageDraw, ImageFont

def bytes_to_pil(image_bytes):
    return Image.open(io.BytesIO(image_bytes)).convert("RGB")

def save_json(detections, out_path):
    with open(out_path, "w") as f:
        json.dump(detections, f, indent=2)

def draw_boxes_and_save(image_bytes, detections, out_path):
    img = bytes_to_pil(image_bytes)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        label = f'{det["class"]} {det["confidence"]:.2f}'
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        draw.text((x1, y1-10), label, fill="white", font=font)
    img.save(out_path, format="JPEG")
