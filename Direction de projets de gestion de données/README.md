# wildfire-fs-project

Description
Wildfire Detection is an application designed to help users identify and report wildfires quickly. Our application uses state-of-the-art computer vision and data analysis techniques to detect fire and smoke in images, providing crucial information to emergency services.

Features
File Upload: Users can upload images containing potential wildfire scenes.
Camera Input: Users can use their phone's camera to capture and analyze images in real-time.
Fire and Smoke Detection: Our application uses a custom-trained YOLOv8 model to detect fire and smoke in images.
Geolocation: If available, the application displays the GPS coordinates of the image, helping emergency services locate the fire.
Weather Information: Users can access weather data related to the detected fire's location, including wind speed and direction.
User-Friendly Interface: The user interface is simple and intuitive, making it easy for anyone to use.
Getting Started
To get started with Wildfire Detection on your local machine, follow these steps:

[API with our trained YOLOv8 model](https://wildfire-project-backend.herokuapp.com)\ == (disabled)
[Streamlit app with our integrated fire&smoke detector for emergency services](https://wildfire-project-streamlit.herokuapp.com/) == (disabled)

link to download the dataset : https://drive.google.com/drive/folders/1oNRu0h1sXO5HsZAXp5kkHgl7SdTRb4zz?usp=sharing

link to download the best model PyTorch (best.pt) : https://drive.google.com/drive/folders/10BBB7h6iRx9Mb9ChAf-tJ4LAD6nj53WE?usp=sharing

Wildfire Detection Application
Final project of data fullstack JEDHA's bootcamp BLOC 6

Prerequisites
Python 3.7 or higher
pip (Python package manager)
Docker (optional)
Installation
Clone the repository to your local machine:

git clone https://github.com/carolinemathius/wildfire-fs-project.git
cd wildfire-fs-project
Set up the frontend and backend environments:

Frontend:

cd frontend
pip install -r requirements.txt
Backend:

cd backend
pip install -r requirements.txt
Usage
Start the backend server:

cd backend
python api.py
The API server will be running at http://localhost:4001.

Start the frontend application:

cd frontend
streamlit run streamlit.py
The Streamlit application will open in your web browser.

Use the application to upload images or capture images with your phone's camera for wildfire detection.

Contributing
We welcome contributions from the community! If you'd like to contribute to this project, please follow these guidelines:

Fork the repository on GitHub.
Clone your forked repository to your local machine.
Make your changes and test them thoroughly.
Create a pull request with a clear description of your changes.
Authors
Anas Maghous
Caroline Mathius
Simon Picard
Thibaut Longchamps
Acknowledgments
We would like to thank the open-source community for providing the tools and libraries that made this project possible.

References
We used the D-Fire Dataset, built by: Pedro Vinícius Almeida Borges de Venâncio, Adriano Chaves Lisboa, Adriano Vilela Barbosa: An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices. In: Neural Computing and Applications, 2022.

API with our trained YOLOv8 model
Streamlit app with our integrated fire&smoke detector for emergency services

About
BLOC 6_Jedha Certification

Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Report repository
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
4
@psimon1
psimon1 Simon P
@Anasmgs
Anasmgs Anas.Mgs
@carolinemathius
carolinemathius
@Thibaut-Longchamps
Thibaut-Longchamps Thibaut Longchamps
Languages
Python
88.2%
 
Dockerfile
11.8%
Suggested workflows
Based on your tech stack
SLSA Generic generator logo
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
Python Package using Anaconda logo
Python Package using Anaconda
Create and test a Python package on multiple Python versions using Anaconda for package management.
Django logo
Django
Build and Test a Django Project
More workflows
Footer
© 2024 GitHub, Inc.
