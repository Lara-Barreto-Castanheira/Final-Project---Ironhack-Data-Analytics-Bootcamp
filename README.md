![Logo](https://github.com/Lara-Barreto-Castanheira/Gynecological-Cytology-Screening-with-Artificial-Intelligence/blob/main/Gynecological%20Cytology%20Screening%20with%20Artificial%20Intelligence_banner.jpg)

# Screening of Gynecological Cytology with Artificial Intelligence

This project aims to develop a system for classifying squamous cells in gynecological cytology using the YOLOv5 deep learning model. The focus of the project is on classifying cells into four distinct classes: Normal, LSIL (Low-grade Squamous Intraepithelial Lesion), HSIL (High-grade Squamous Intraepithelial Lesion), and Carcinoma. The developed system is implemented as an interactive Streamlit application, allowing users to upload images for diagnostic prediction.

## Importance of Gynecological Cytology in Pathology
Gynecological cytology, commonly known as the Pap smear, is an essential tool for the early detection of cellular changes in the cervix, including precancerous lesions and cervical cancer. Early detection is critical to increasing the chances of effective treatment and improving patient survival rates. With the advent of artificial intelligence techniques, it's possible to automate and enhance the screening process, reducing human error and increasing diagnostic efficiency.

## Project Structure
### 1. Data Collection and Preparation
Initially, images of squamous cells were collected and categorized into four classes: Normal, LSIL, HSIL, and Carcinoma. Roboflow was then used to organize and prepare the final dataset, including the annotation and labeling of images. The dataset was split into training, validation, and test sets.

### 2. YOLOv5 Setup
The YOLOv5 model was chosen for the task of cell detection and classification. The YOLOv5 repository was downloaded from the official Ultralytics GitHub, along with its requirements. A YAML configuration file was created to specify the location of images, labels, and classes. This file was placed in the data folder within the YOLOv5 directory.

### 3. Environment Setup
A virtual environment was created using Conda to manage the project's dependencies. YOLOv5 and PyTorch requirements were installed within this environment.

### 4. Model Training
The YOLOv5 model was trained using the prepared datasets. During training, parameters were carefully tuned to avoid overfitting, ensuring that the model generalized well to new data.

### 5. Development of the Streamlit Application
A Streamlit application was developed to facilitate interaction with the model. The app allows users to view the type of cell studied, common cytological findings, and upload new images for real-time diagnostic prediction.

## Requirements
* Python 3.8 or higher
* Conda
* PyTorch
* YOLOv5
* Roboflow
* Streamlit

## Installation
### * 1. Create a Conda environment:

conda create -n yolov5_env python=3.8
conda activate yolov5_env

### * 2. Install the requirements:

pip install -r requirements.txt

### * 3. Clone the YOLOv5 repository from Ultralytics:

git clone https://github.com/ultralytics/yolov5

### * 4. Navigate to the project directory:

!cd yolov5

### * 5. Add the YAML configuration file to the data Yolov5 folder.

### * 6. Train the model as needed:

!cd yolov5 && python train.py --img 640 --batch 16 --epochs 50 --data data/your_file.yaml --weights yolov5s.pt


## Using the Streamlit Application
### * 1.Ensure you are in the Conda environment (yolov5_env).

### * 2.Run the application:
  
  streamlit run your_application.py

### * 3.Access the link provided by Streamlit to interact with the application.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Lara Castanheira 


