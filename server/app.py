from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = FastAPI()

# Define allowed origins
origins = [
   "*"
]

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Load the saved CNN model
model = tf.keras.models.load_model("models/Custom_ResNet.h5")

def preprocess_image(file):
    # Open the image file
    img = Image.open(file)

    # Resize the image to match the input shape
    img = img.resize((64, 64))  # Adjust the size to match the model's input shape

    # Convert the image to RGB if it's not already in RGB format
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Convert to NumPy array
    img_array = np.array(img)

    # Perform mean subtraction and standard deviation normalization
    img_array = img_array.astype('float32')
    img_array -= np.mean(img_array)
    img_array /= np.std(img_array)

    # Add a batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

def predict_skin_condition(processed_image):
    # Perform inference
    prediction = model.predict(processed_image)

    return prediction.tolist()

def get_predicted_class(prediction_result):
    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(prediction_result)

    # Map the index to the corresponding class name
    class_names = ['Actinic Keratosis', 'Squamous Cell Carcinoma', 'Melanoma', 'Basal Cell Carcinoma', 'Vascular Lesion']
    predicted_class = class_names[predicted_class_index]

    return predicted_class

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        processed_image = preprocess_image(io.BytesIO(contents))
        prediction_result = predict_skin_condition(processed_image)
        predicted_class = get_predicted_class(prediction_result)
        # Provide meaningful descriptions based on predicted class
        description = "Default Placeholder description"
        reme1 = reme2 = reme3 = ""
        if predicted_class == "Actinic Keratosis":
            description = "Actinic keratosis is a precancerous skin lesion that develops due to excessive exposure to ultraviolet (UV) radiation from sunlight or tanning beds."
            reme1 = "Cryotheraphy: Freezing the lesion"
            reme2 = "Topical chemotherapy: Application of medicine to the skin"
            reme3 = "3.	Curettage : Damaged portion is scraped off"
        elif predicted_class == "Squamous Cell Carcinoma":
            description = "SCC is the second most common skin cancer, typically arising from sun-exposed areas. This usually looks like a bump or a scaly sore"
            reme1 = "Surgery: Removal of the lesion"
            reme2= "Chemotherapy: For advanced cases"
            reme3="Targeted Therapy: Medicines attacking specific chemicals in cancer cells."
        elif predicted_class == "Basal Cell Carcinoma":
            description = "BCC is a type of skin cancer that affects basal cells in the lower epidermis. It constitutes about 80%% of skin cancer diagnoses"
            reme1 = "Freezing: Using liquid nitrogen"
            reme2 = "Curettage and electrodessication"
            reme3 = "4.	Mohs micrographic surgery: All the cancer cells are removed by examining small amounts of tissue until the cancer cells are found"
        elif predicted_class == "Vascular Lesion":
            description = "Vascular lesions affect blood vessels and can appear as visible marks on the skin."
            reme1 = "Light-Based and Laser Treatments: Heat capillaries within the lesion to clear them"
            reme2 = "Alma: Alma offers safe treatments for different skin types with minimal pain and fast results"
        elif predicted_class == "Melanoma":
            description = "Melanoma is a malignant skin cancer that originates from melanocytes (pigment-producing cells)"
            reme1= "Immunotherapy: Boosts the immune system to fight cancer cells."
            reme2 = "Targeted Therapy: Targets specific genetic mutations"
            reme3 = "Surgical Excision: Removal of the melanoma and surrounding tissue."
        else:
            predicted_class = "Try Another Image"
            # description = ""
        return {"prediction": predicted_class, "prediction_desc": description, "treat1":reme1, "treat2":reme2, "treat3":reme3}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
