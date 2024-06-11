import streamlit as st
import pandas as pd
import pickle
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import torch
import os


st.sidebar.header('Library')
option=st.sidebar.selectbox("Choose an option",("Normal squamous cells","LSIL - Low-grade squamous intraepithelial lesion","HSIL - High-grade squamous intraepithelial lesion","Squamous cell carcinoma","Diagnosis Prediction"))

st.title("Gynecological Cytology screening with Artificial Intelligence")
st.write("This is a cytology screening application that uses AI to analyse uploaded gynaecological cytology images, providing diagnostic results based on **Bethesda System**")

#col1, col2 = st.columns([1, 2])
#with col1:
    #st.header("Bethesda System")
#with col2:
    #st.image("https://m.media-amazon.com/images/I/41RNNakgYCL._SY445_SX342_.jpg", width= 200)


#Normal squamous cells

if option=="Normal squamous cells":

    st.title("Normal squamous cells")

    st.write("---")
    st.header("Cytology findings")

    image_url = 'https://www.garciaureta.com/wp-content/uploads/2018/12/0002-9-464x331.jpg'
    st.image(image_url, caption='Normal superficial and intermediate squamous cells', use_column_width=True) 


    st.subheader("Superficial cells")
    st.write("""**Location**: Outermost layer of non-keratinised epithelium
                \n**Shape**: Polygonal
                \n**Cytoplasm**: Eosinophilic
                \n**Nucleus**:
                \n- **Location**: Central
                \n- **Characteristics**: Pyknotic 
                \n**Phases of the Menstrual Cycle**:
                \n- Abundant in the late proliferative and ovulatory phases
                \n- Estrogen at maximum levels""")

    st.write("---")
    
    st.subheader("Intermediate Squamous Cells")
    st.write("""**Location**: Layer of the stratum spinosum (middle zone) of the squamous epithelium
                \n**Shape**: Polygonal
                \n**Cytoplasm**:
                \n- Thin and transparent, usually basophilic
                \n**Nucleus**:
                \n- **Location**: Central
                \n- **Characteristics**: Fine granular and evenly dispersed chromatin
             
                \n**Phases of the Menstrual Cycle**:
                \n- Abundant when progesterone levels are high""")

    st.write("---")

    st.markdown("""This page shows the features of normal squamous cells""")

    #if st.button("LSIL - Low-grade squamous intraepithelial lesion"):
        #selected_buton = "LSIL - Low-grade squamous intraepithelial lesion"

##LSIL
if option=="LSIL - Low-grade squamous intraepithelial lesion":

    st.title("LSIL - Low-grade squamous intraepithelial lesion")

    st.write("---")
    st.header("Cytology findings")

    image_url = 'https://www.pathologyoutlines.com/imgau/cervixLSILsalih06.jpg'
    st.image(image_url, caption='LSIL - Low-grade squamous intraepithelial lesion', use_column_width=True) 

    st.write("""**Cell type**: Large, mature cells (equal in size to a normal superficial or intermediate squamous cell)
             \n**Cytoplasm**:
             \n- Abundant
             \n- Isolated cells or in groups
             \n- Cytoplasmic cavities (koilocytes): viral cytopathic characteristis
             \n- Clear, broad and sharply delineated perinuclear zone and a peripheral rim of densely stained cytoplas
             \n- Dense, eosinophilic cytoplasm with increased keratinisation and little or no evidence of koilocytos
             
             \n**Nucleus**:
             \n- Nuclear atypia
             \n- Nuclear enlargement > 3x the area of normal intermediate nucleus
             \n- Low but slightly increased N/C ratio
             \n- Usually hyperchromatic
             \n- Anisonucleosis
             \n- Coarsely granular, spotted or densely opaque chromatin
             \n- Variable nuclear contours, from smooth to very irregular
             \n- Binucleation and multinucleation
             \n- Nucleolus absent""")
    
    st.write("---")

    st.markdown("""This page shows the features of LSIL""")

#HSIL
if option=="HSIL - High-grade squamous intraepithelial lesion":

    st.title("HSIL - High-grade squamous intraepithelial lesion")

    st.write("---")
    st.header("Cytology findings")

    image_url = 'https://www.pathologyoutlines.com/imgau/cervixHSILcytologyChornenkyy01.png'
    #st.image(image_url, caption='HSIL - Low-grade squamous intraepithelial lesion', use_column_width=True) 
    st.image(image_url, width=500,caption='HSIL - Low-grade squamous intraepithelial lesion') 
    st.write("""**Cell type**:
             \n- Small (Approximately the size of the parabasal cells)
             \n- Isolated cells, in sheets or in syncytium-like clusters (appearing as hyperchromatic clustered groups)
             
             \n**Nucleus**:
             \n- Nuclear atypia
             \n- Nuclear enlargement
             \n- Irregular nuclear contour with nuclear bites
             \n- Generally hyperchromatic, but can be normochromatic or hypochromatic
             \n- Chromatin can be fine or coarsely granular and evenly distributed
             \n- Absence of nucleolus

             \n**Cytoplasm**:
             \n- Decreased cytoplasmic area leading to a high N/C ratio
             \n- Can be immature, delicate or densely metaplastic or mature / densely keratinised
             
             \n**Type of aggregate**:
             \n- Syncytium-like / clustered hyperchromatic groups""")

    st.write("---")

    st.markdown("""This page shows the features of HSIL""")


#Carcinoma
if option=="Squamous cell carcinoma":

    st.title("Squamous cell carcinoma")

    st.write("---")
    st.header("Cytology findings")

    image_url = 'https://img.medscapestatic.com/pi/meds/ckb/71/38171tn.jpg'
    st.image(image_url, caption='Squamous cell carcinoma', use_column_width=True) 
    #st.image(image_url, width=400,caption='HSIL - Low-grade squamous intraepithelial lesion') 
    st.write("""**Cell type**:
             \n- Large to medium-sized non-keratinised cells with a high N/C ratio
             \n- Rare single keratinised cells can be seen
            
             \n**Nucleus**:
             \n- Round nucleus with irregular contours, coarse, irregularly distributed chromatin and macronucleoli
             \n- Bare nucleus
             \n- Markedly hyperchromatic nucleus with irregular granular chromatin
             \n- Rare nucleolus
             
             \n**Cytoplasm**:
             \n- Sparse and dense basophilic cytoplasm without keratinisation
             \n- Irregularly shaped keratinised cells with orange-philic cytoplasm, often with scaly pearls
             \n- Tadpole-shaped cells and keratohyalin granules in the cytoplasm
             
             \n**Aggregate type**:
             \n- Agglomerated groups and syncytial fragments
             
             \n**Background**: 
             \n- Cell specimens, usually with background tumour diathesis (fresh or haemolysed blood and necrotic cell debris)
             \n- Tumour diathesis may not be observed in tumours with a depth of invasion of less than 5 mm or in exophytic tumours 
Non-keratinising variants""")

    st.write("---")

    st.markdown("""This page shows the features of squamous cell carcinoma""")

#Diagnosis
if option=="Diagnosis Prediction":

    st.title("Diagnosis Prediction")

    st.header("Diagnosis based on image inference with the YOLO v5 model")


#Model
    def load_model():
        model = torch.hub.load('ultralytics/yolov5', 'custom', path= r'C:\Users\Lara\Documents\Ironhack\Course\final_project_gyncit_4\yolov5\runs\train\custom_yolov5\weights\best.pt') 
        return model

    model = load_model()

    #Function to do the inference
    def predict(image):
        results = model(image)
        return results

    st.write("Upload an image to predict the diagnosis")

    #Load the image
    uploaded_file = st.file_uploader("Pick an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Loaded image', use_column_width=True)
        st.write("")
        st.write("Making the inference...")

        # Convert the image to the format required for YOLOv5
        image = np.array(image)

        # Making the inference
        results = predict(image)

        # Show results
        #st.write(results.pandas().xyxy[0])  # Show results as pandas dataframe

        # Plot results on the image
        results.render()  # Update the image with bounding boxes and labels
        annotated_image = Image.fromarray(results.render()[0])
        st.image(annotated_image, caption='Image with predicted diagnosis', use_column_width=True)
    
    st.write("---")
    st.markdown("""This app alows us to predict the diagnosis based on images inference""")
