# 🔥 Wildfire-FS – Fire & Smoke Detection Assistant

Wildfire-FS is a computer vision application designed to detect fire and smoke in images and help users quickly report potential wildfires.
It combines a YOLOv8 model, geolocation, and weather data to provide useful context to emergency services.
---
## Project Overview

This project provides an end-to-end pipeline for **wildfire detection**:

A backend API serving a custom-trained YOLOv8 model (fire & smoke detection).
A Streamlit frontend that lets users:

- upload images,
- capture images from their phone (via browser),
- visualize detections.

Optional geolocation & weather information for the detected fire location.

A simple UX so the tool can be used by non-technical users (citizens, emergency operators).

🌐 Deployed apps (Heroku) are currently disabled, but links are kept for reference.

API with YOLOv8 model (disabled):
```bash
https://wildfire-project-backend.herokuapp.com
```
Streamlit app for emergency services (disabled):
```bash
https://wildfire-project-streamlit.herokuapp.com/
```
---
## 🎯 Objectives

Detect fire and smoke automatically from images using a YOLOv8 model.
Support emergency services with:

- approximate location (GPS coordinates, when available),
- relevant weather information (wind, etc.).
- Provide a simple, user-friendly interface that works from desktop or mobile.

Showcase an end-to-end Computer Vision project (data → model → API → frontend).

---

## Model & Dataset

Model: custom-trained YOLOv8 object detector

Classes: typically **fire**, **smoke**, **background**

---

## Dataset: D-Fire Dataset

Built by: Pedro Vinícius Almeida Borges de Venâncio, Adriano Chaves Lisboa, Adriano Vilela Barbosa

Paper: “An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices”, Neural Computing and Applications (2022).

---

## Downloads

📁 Dataset (D-Fire subset used in the project):
```bash
https://drive.google.com/drive/folders/1oNRu0h1sXO5HsZAXp5kkHgl7SdTRb4zz?usp=sharing
```
---

## Best PyTorch YOLOv8 model (best.pt):
```bash
https://drive.google.com/drive/folders/10BBB7h6iRx9Mb9ChAf-tJ4LAD6nj53WE?usp=sharing
```
---

## Key Features

- Image Upload
- Upload pictures containing potential wildfire scenes.
- Camera Input
- Capture and analyze images directly from your phone or laptop camera.
- Fire & Smoke Detection

Inference using a YOLOv8 model trained on wildfire datasets.
Bounding boxes and labels displayed on the image.
Geolocation (if available)

Read / display GPS coordinates associated with the image.
Useful to localize the fire for emergency services.

---

## Tech Stack

Language Python 3.7+

Computer Vision & ML YOLOv8 (PyTorch-based)
OpenCV / PIL (for image handling – depending on implementation)

Backend
Python API (api.py) – e.g. FastAPI/Flask (depending on your implementation)
Exposes an endpoint to run YOLOv8 inference on images

Frontend
Streamlit app (streamlit.py)
Infrastructure
Docker (optional, for containerized deployment)

(Previously) Heroku for deployment of:

Backend API
Streamlit frontend

---

🗂️ Project Structure
```text
wildfire-fs-project/
├── backend/
│   ├── api.py                # Backend API serving YOLOv8 model
│   └── requirements.txt      # Backend dependencies
│
├── frontend/
│   ├── streamlit.py          # Streamlit UI (upload, camera, display results)
│   └── requirements.txt      # Frontend dependencies
│
├── Dockerfile                # (Optional) Docker configuration (if monolithic)
├── README.md                 # This file
└── ...                       # Other project files, configs, notebooks, etc.
```
---

## 🚀 Getting Started (Local)
✅ Prerequisites

Python 3.7+
pip

---

## Docker

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/carolinemathius/wildfire-fs-project.git](https://github.com/Thibaut-Longchamps/Certification-Fullstack/tree/main/Direction%20de%20projets%20de%20gestion%20de%20donn%C3%A9es)
cd wild fire project
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
# macOS / Linux
```bash
source venv/bin/activate
```
# Windows
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```
Frontend
```bash
cd ../frontend
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Local Usage

### ▶️ 1. Start the Backend API

From the backend/ folder:
```bash
cd backend
docker build -t wildfire-backend .
docker run -d --name wildfire-backend -p 4001:4001 wildfire-backend
```
The API should be available at:
```bash
http://localhost:4001 (according to the project setup)
```
This service handles YOLOv8 inference on images (upload/call from Streamlit).

### ▶️ 2. Start the Streamlit Frontend

From the frontend/ folder:
```bash
cd ../frontend
docker build -t wildfire-frontend .
docker run -d --name wildfire-frontend -p 8501:8501 wildfire-frontend
```

## Authors

- Anas Maghous
- Caroline Mathius
- Simon Picard
- Thibaut Longchamps

## 📚 About

This project was developed as part of BLOC 6 – Jedha Certification (Wildfire Detection Project).

