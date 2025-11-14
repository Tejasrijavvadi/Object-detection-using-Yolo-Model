# PAS vs Bitewing Classifier

This project implements a deep learning classifier to distinguish between PAS and Bitewing images using **PyTorch** and **ResNet50**.

---

## Table of Contents

1. [Project Structure](#project-structure)  
2. [Dataset Preparation](#dataset-preparation)  
3. [Image Preprocessing & Augmentation](#image-preprocessing--augmentation)  
4. [Normalization](#normalization)  
5. [Training](#training)  
6. [Inference](#inference)  
7. [Dataset Balancing](#dataset-balancing)  
8. [Results Visualization](#results-visualization)  
9. [Dependencies](#dependencies)

---

## Project Structure

```
PAsVSBitewing/
├── Code/
│   ├── train.py              # Training script
│   ├── inference.py          # Inference script
│   ├── preprocess_images.py  # Optional preprocessing & augmentation
│   ├── balancedata.py        # Optional dataset balancing script
│   ├── getNormalisation_stats.py  # Normalization stats calculation
│   └── config.json           # Configuration file
├── data/
│   └── PasvsBitewing/
│       ├── PAS/
│       ├── Bitewing/
├── Model/
│   └── pavsbitewing.pth     # Saved trained model
└── README.md
```

---

## Dataset Preparation

- Dataset contains images in two classes: `PAS` and `Bitewing`.
- Example folder structure:

```
PasvsBitewing/
├── PAS/
│   ├── img1.JPG
│   └── img2.JPG
├── Bitewing/
│   ├── img1.JPG
│   └── img2.JPG
```

---

## Image Preprocessing & Augmentation

- Images are preprocessed to resize to `(IMG_SIZE x IMG_SIZE)`
- Optional augmentations: horizontal flips, small rotations for balancing classes
- Preprocessing ensures uniform input size for training and inference

```python
ROTATED_OUTPUT_PATH = os.path.join(DATASET_BASE_PATH, "processed/images")
MASK_OUTPUT_PATH = os.path.join(DATASET_BASE_PATH, "processed/masks")
```

---

## Normalization

- Compute dataset-specific mean and std using `getNormalisation_stats.py` or precomputed values in `config.json`:

```json
"normalize_mean": [0.485, 0.456, 0.406],
"normalize_std":  [0.229, 0.224, 0.225]
```

- Pretrained ResNet50 expects 3-channel input. ImageNet normalization is acceptable.

---

## Training

- Training uses `train.py`:
  - **Model:** ResNet50 pretrained on ImageNet  
  - Only final fully connected layer is trainable  
  - Optimizer: Adam  
  - Loss: CrossEntropyLoss  
  - Dataset split: Train / Validation / Test  
- Training outputs:
  - Best validation accuracy
  - Loss & accuracy curves
  - Saved model: `Model/pavsbitewing.pth`

```bash
python train.py
```

---

## Inference

- Use `inference.py` to predict a single image:

```python
from inference import predict_image
predict_image("path_to_image.JPG")
```

- The script:
  - Loads trained ResNet50 model  
  - Applies same transformations as training  
  - Shows image with predicted class and confidence

---

## Dataset Balancing

- Optional preprocessing/augmentation can be used to balance dataset classes:
  - Resize all images to the same dimensions  
  - Apply horizontal flips or small rotations  
- Ensures no class dominates training

---

## Results Visualization

- Training metrics (loss & accuracy) plotted per epoch
- Confusion matrix for test set shows class-wise accuracy
- Inference displays image with predicted class and confidence

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

1. **Compute normalization stats (optional):**  
```bash
python getNormalisation_stats.py
```
2. **Train model:**  
```bash
python train.py
```
3. **Run inference:**  
```bash
python inference.py
```

---

This README provides a **complete step-by-step overview** of the PAS vs Bitewing Classifier pipeline, including preprocessing, training, normalization, inference, and dataset balancing.