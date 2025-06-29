# Face Recognition Using Raspberry Pi

A real-time face recognition system built on Raspberry Pi using OpenCV, PCA (Eigenfaces), and SVM for secure biometric access control. Developed as part of ECE 3200 coursework at Khulna University of Engineering & Technology (KUET).

## 🔍 Project Overview

This project demonstrates how face recognition can be implemented on a lightweight embedded system like Raspberry Pi. The system:
- Captures facial images via Pi Camera.
- Uses PCA to extract Eigenfaces from grayscale images.
- Trains an SVM classifier to distinguish between registered users.
- Performs real-time face recognition and determines access based on recognition confidence.

## 🔍 Project Summary

- **Goal**: Secure face authentication system using Raspberry Pi and camera.
- **Method**: PCA for dimensionality reduction, SVM for classification.
- **Result**: 94.74% accuracy on large datasets.

## 📁 Project Structure

- `src/`: All scripts including dataset creation, training, and recognition.
- `report/`: Course project report PDF.
- `models/`: Saved SVM and PCA models.
- `dataset/`: Sample training images.


## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Run Scripts

# Capture facial images for training
python src/dataset_creation.py

# Train the PCA + SVM model
python src/train_svm.py

# Start real-time face recognition
python src/recognize_face.py

## 📊 Technologies Used

- Python
- OpenCV
- Raspberry Pi + PiCamera
- PCA (Principal Component Analysis)
- SVM (Support Vector Machine)
- scikit-learn, NumPy, Pillow

## 📜 Report

Read the full documentation here: 📄 report/face-recognition.pdf

## 👥 Authors

- **Md. Sadman Sakib** (1509050)  
- **Md. Imran Hasan** (1509049)  
  *Department of ECE, KUET*

**Supervisor:**  
- Mr. Tasnim Azad Abir, Assistant Professor

## 🚀 Future Scope

- 🔬 IR camera for nighttime recognition
- 🌐 GSM/IoT integration for remote alerts
- 🏫 Smart surveillance, attendance systems, and beyond.

##🌟 License

This project is for academic and learning purposes. Contact authors for inquiries.
