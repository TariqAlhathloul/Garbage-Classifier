
# Real-Time Garbage Classification and Sorting System Using Deep Learning

## Overview
This project aims to address the global challenge of waste management using **Deep Learning** and **Computer Vision**. It implements a real-time garbage classification system that uses the **YOLO algorithm** to classify waste into seven categories and further groups them into **recyclable** and **non-recyclable** categories. The trained model is deployed on a **Raspberry Pi 5** with a camera and an LCD screen for real-time detection and classification.

---

## Features
- **Real-Time Detection**: Uses YOLO for accurate and fast garbage classification.
- **Classification Categories**:
  - **Recyclable**: CARDBOARD, PAPER.
  - **Non-Recyclable**: PLASTIC, METAL, GLASS, CLOTH, BIODEGRADABLE.
- **Edge Deployment**: Runs on a Raspberry Pi 5 for portability and scalability.
- **User-Friendly Output**: Displays results ("Recyclable" or "Non-Recyclable") on an LCD screen.

---

## Dataset
[link to the dataset](https://universe.roboflow.com/material-identification/garbage-classification-3/dataset/2)

The project uses an open-source dataset with the following 7 classes:
- **BIODEGRADABLE**
- **CARDBOARD**
- **CLOTH**
- **GLASS**
- **METAL**
- **PAPER**
- **PLASTIC**

### Dataset Preprocessing
- Resized and normalized images.
- Applied data augmentation techniques (flipping, rotation).

---

### Hardware
- **Raspberry Pi 5**: The core computing device.
- **Camera Module**: Captures real-time images of waste.
- **LCD Screen**: Displays the classification results.
- **Servo Motor***: Open and closes the waste baskets

- **YOLOv8 Framework**: For garbage detection and classification.
- **pytorch**: Deep learning framework.
- **OpenCV**: Image processing library.
- **Python**: Programming language.

---

## System Workflow
1. The Raspberry Pi camera captures an image of waste.
2. The YOLO model classifies the waste into one of the seven predefined categories.
3. The classification is mapped to **Recyclable** or **Non-Recyclable**.
4. The result is displayed on the LCD screen.

---

## Installation

### Prerequisites
- Raspberry Pi 5 with a camera module.
- Python 3.7 or later.
- LCD screen connected to the Raspberry Pi.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/garbage-classification.git
   ```
  
3. Enter the project directory:
    ```bash
    cd garbage-classification
    ```
3. Create virtual environment and activate it:
    ```bash
    python -m venv project_venv
    source project_venv/bin/activate
    ```

4. install the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the detection script:
    ```bash
    python dectet.py