# PAS Rotation Classifier

This project implements a deep learning classifier to detect different rotation positions (Lower, Left Oriented, Upper) of PAS images using **PyTorch** and **ResNet50**.

---

## Table of Contents

1. [Project Structure](#project-structure)  
2. [Dataset Preparation](#dataset-preparation)  
3. [Image Preprocessing](#image-preprocessing)  
4. [Normalization](#normalization)  
5. [Training](#training)  
6. [Inference](#inference)  
7. [Dataset Balancing](#dataset-balancing)  
8. [Results Visualization](#results-visualization)  
9. [Dependencies](#dependencies)

---

## Project Structure

```
PASRotationClassifier/
├── Code/
│   ├── train.py              # Training script
│   ├── inference.py          # Inference script
│   ├── preprocess_images.py  # Preprocessing & rotation script
│   ├── balancedata.py  # balanace data script
│   ├── getNormalisation_stats.py  # normalisation and standard deviation
│   └── config.json           # Configuration file
├── data/
│   └── PAs_diff_position_dataset/
│       ├── Lower/
│       ├── Left oriented/
│       ├── Upper/
│       └── Masks/            # Optional masks
├── Model/
│   └── pasrotation.pth       # Saved trained model
└── README.md
```

---

## Dataset Preparation

- Dataset contains images in three rotation classes: `Lower`, `Left oriented`, `Upper`.
- Optional mask images can be provided in a `Masks` folder (aligned with images).
- Example folder structure:

```
PAs_diff_position_dataset/
├── Lower/
│   ├── img1.png
│   └── img2.png
├── Left oriented/
├── Upper/
└── Masks/
```

---

## Image Preprocessing

- Images are processed using **`preprocess_images.py`**:
  - Rotate images according to class rules:
    - `Lower`: 0°  
    - `Left oriented`: 90°  
    - `Upper`: 180°  
  - Resize to `(IMG_SIZE x IMG_SIZE)`  
  - Save processed images in `processed/images`  
  - Optional masks are rotated and resized in `processed/masks`  
- Processed images are ready for training.

```python
ROTATED_OUTPUT_PATH = os.path.join(DATASET_BASE_PATH, "processed/images")
MASK_OUTPUT_PATH = os.path.join(DATASET_BASE_PATH, "processed/masks")
```

---

## Normalization

- Compute dataset-specific mean and standard deviation using `get_normalization_stats.py` (or precomputed in `config.json`):

```json
"normalize_mean": [0.4576, 0.4576, 0.4576],
"normalize_std":  [0.1931, 0.1931, 0.1931]
```

- Since images are grayscale stored in RGB format, all channels have identical mean & std.
- Pretrained ResNet50 expects 3-channel input. Using ImageNet normalization is also acceptable.

---

## Training

- Training uses `train.py`:
  - **Model:** ResNet50 pretrained on ImageNet  
  - Only final fully connected layer is trainable  
  - Optimizer: Adam  
  - Loss: CrossEntropyLoss  
  - Dataset split: Train / Validation / Test  
  - Data augmentations: random horizontal flip, small rotations
- Example command:

```bash
python train.py
```

- Training outputs:
  - Best validation accuracy
  - Loss & accuracy curves plotted
  - Saved model: `Model/pasrotation.pth`

---

## Inference

- Use `inference.py` to predict a single image:

```python
from inference import predict_image

predict_image("path_to_image.png")
```

- The script:
  - Loads trained ResNet50 model  
  - Applies same transformations as training  
  - Shows image with predicted class and confidence

---

## Dataset Balancing

- Preprocessing allows to balance classes:
  - All classes resized to same dimensions  
  - Upsampling technique used 
- Ensures no class dominates the training process

---

## Results Visualization

- Training metrics (loss & accuracy) are visualized per epoch
- Confusion matrix for test set shows class-wise accuracy
- Inference displays image with predicted class and confidence percentage

---

## Dependencies

- Python 3.8+  
- PyTorch 2.x  
- torchvision  
- PIL (Pillow)  
- matplotlib  
- seaborn  
- scikit-learn  
- numpy  

Install dependencies:

```bash
pip install torch torchvision pillow matplotlib seaborn scikit-learn numpy
```

---

## Usage Workflow

1. **Preprocess dataset:**  
```bash
python preprocess_images.py
```

2. **Compute normalization stats (optional):**  
```bash
python get_normalization_stats.py
```

3. **Train model:**  
```bash
python train.py
```

4. **Run inference:**  
```bash
python inference.py
```

---

This README provides a **complete step-by-step overview** of your PAS Rotation Classifier pipeline, including preprocessing, training, normalization, inference, and dataset balancing.