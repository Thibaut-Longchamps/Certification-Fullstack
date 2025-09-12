# MovePort Dataset – Multimodal Activity Recognition

## Objective
Develop a **pipeline for multimodal time-series analysis** using EMG, IMU, IPS, and MoCap sensors to classify human activities and compare unified vs. modality-specific deep learning architectures.

---

## Dataset
**MovePort Dataset** includes:

- **EMG** (Electromyography)  
- **IMU** (Inertial Measurement Unit)  
- **IPS** (Insole Pressure Sensors)  
- **MoCap** (Motion Capture)  

**25 participants** performing:

- `back` – backward lean  
- `forward` – forward lean  
- `halfsquat` – half squat  
- `still` – standing still  

**Source:** [FigShare](https://figshare.com/articles/dataset/MovePort_Multimodal_Dataset_of_EMG_IMU_MoCap_and_Insole_Pressure_for_Analyzing_Abnormal_Movements_and_Postures_in_Rehabilitation_Training/25202183?file=46577461)  
**Paper:** [IEEE Xplore](https://ieeexplore.ieee.org/document/10601196)

---

## Workflow
1. **Data Loading & Preprocessing**
   - Load raw data from each modality.  
   - Align and resample to 20 Hz.  
   - Correct feature names and save processed CSVs.  

2. **Data Alignment & Formatting**
   - Ensure temporal alignment across modalities.  
   - Add metadata: participant, activity, timestamp.  
   - Create unified labels for supervised learning.  

3. **Modeling & Training**
   - Prepare training/testing sets.  
   - Compare **unified** vs. **modality-specific** deep learning models (e.g., CNNs).  
   - Evaluate with accuracy, F1-score, and confusion matrices.  

---

## Key Techniques
- **Resampling:** Align different sensor frequencies (EMG 2000 Hz, IMU 100 Hz, IPS 60 Hz, MoCap 100 Hz)  
- **Multimodal Fusion:** Combine features from all modalities  
- **Deep Learning:** Keras/TensorFlow  
- **Hyperparameter Tuning:** `keras-tuner`

---

## Repository Structure
data/ # Raw data (not included)
data_processed/ # Processed CSV files
data_training/ # Preprocessed arrays for training
ATC_Final_notebook.ipynb # Main notebook
README.md

---
## How to Run
1. Download the dataset from FigShare and extract into `data/`.  
2. Install dependencies: `pip install -r requirements.txt`.  
3. Run `ATC_Final_notebook.ipynb` step by step.  

> Note: Notebook includes code for downloading and preprocessing data. Uncomment if needed.
---
## Citation
Please cite:  
*"MovePort: Multimodal Dataset of EMG, IMU, MoCap and Insole Pressure for Analyzing Abnormal Movements and Postures in Rehabilitation Training", IEEE Xplore.*
