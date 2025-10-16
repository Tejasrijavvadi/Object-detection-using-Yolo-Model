# Object-detection-using-Yolo-Model
Developed a two-microservice system using FastAPI forobject detection. The AI Backend uses YOLOv8 to perform inference on uploaded images, generating both annotated output images and structured JSON detections (class, confidence, bounding box). The UI Backend provides a simple upload interface and communicates with the AI backend via HTTP.

#  Object Detection using YOLOv8 + FastAPI Microservices

Developed a **two-microservice system** using **FastAPI** for object detection.  
The **AI Backend** uses **YOLOv8** to perform inference on uploaded images, generating annotated output images and structured JSON detections (class, confidence, bounding box).  
The **UI Backend** provides a simple upload interface and communicates with the AI Backend via HTTP.



## Project Overview

This project demonstrates an end-to-end **object detection pipeline** using **Ultralytics YOLOv8**, split into two independent FastAPI services:

- **AI Backend (`ai-backend/`)** – handles model loading, inference, and returns detection results.  
- **UI Backend (`ui-backend/`)** – provides a minimal web UI for image upload and result display.

Each service runs separately but communicates via REST API calls.



## Folder Structure

```
Object-detection-using-Yolo-Model/
│
├── ai-backend/
│   ├── app.py                # FastAPI app for YOLOv8 inference
│   ├── utils.py              # Helper utilities for inference
│   ├── requirements.txt      # Python dependencies for AI service
│   └── models/
│       └── yolov8n.pt        # YOLOv8 weights (not uploaded)
│
├── ui-backend/
│   ├── app.py                # FastAPI app for UI service
│   ├── templates/
│   │   └── index.html        # Upload and display interface
│   ├── static/               # Optional static assets
│   └── requirements.txt      # Python dependencies for UI service
│
├── test_images/              # Sample test images
├── outputs/                  # Annotated results and JSON detections
├── batch_process.py          # Script for batch inference
├── .gitignore
└── README.md
```

---

##  Technologies Used

| Category | Tools |
|-----------|-------|
| Language | Python 3.10 + |
| Frameworks | FastAPI, Starlette |
| Model | Ultralytics YOLOv8 |
| Server | Uvicorn |
| Utilities | Pillow (PIL), NumPy |
| Frontend | HTML + Jinja2 |
| Environment | Windows / VS Code |

---

##  Setup Instructions

### 1️ Clone the repository
```bash
git clone https://github.com/Tejasrijavvadi/Object-detection-using-Yolo-Model.git
cd Object-detection-using-Yolo-Model
```

### 2️ Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate           # Windows
# source .venv/bin/activate      # Linux / macOS
```

### 3️ Install dependencies

**AI Backend:**
```bash
cd ai-backend
pip install -r requirements.txt
```

**UI Backend:**
```bash
cd ../ui-backend
pip install -r requirements.txt
```

---

### 4️ Run the services

**Start AI Backend**
```bash
cd ai-backend
uvicorn app:app --host 0.0.0.0 --port 8001 --reload
```

**Start UI Backend**
```bash
cd ../ui-backend
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Then open:  
 **http://127.0.0.1:8000**

You’ll see the upload page where images can be sent to the AI Backend for inference.

---

### 5️ (Optional) Run batch inference
```bash
python batch_process.py
```
Outputs (annotated + JSON) are saved in the `outputs/` folder.

---

##  Example Output

When an image is uploaded, the model returns detections such as:

```json
{
  "detections": [
    { "class": "person", "confidence": 0.91, "bbox": [120, 150, 340, 480] },
    { "class": "car", "confidence": 0.88, "bbox": [420, 200, 680, 480] }
  ]
}
```

Annotated images are also produced with bounding boxes and labels.

---

##  Example API (AI Backend)

**Endpoint**

```
POST /detect
```

**Request**
- `multipart/form-data` → image file

**Response**
- JSON with detection results (class, confidence, bounding box)

---

##  Key Features

-  YOLOv8-based object detection  
-  Modular microservice architecture (AI + UI)  
-  Real-time inference via REST API  
-  Simple upload interface  
-  Batch processing option  
-  JSON + image outputs  
-  Easily extendable and Docker-ready  

---

##  Future Enhancements

-  Containerize with Docker Compose  
-  Add authentication to APIs  
-  Support video / webcam streams  
-  Host model weights on cloud storage  
-  Deploy on AWS / Azure / Render  

---

##  License
This project is licensed under the **MIT License**.

---

## 👩 Author

**Tejasri Javvadi**  
 *[tejasridevi30954@gmail.com]*  
 [GitHub Profile](https://github.com/Tejasrijavvadi)

---

 *If you find this project useful, please star the repository!*
