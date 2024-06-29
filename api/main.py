import numpy as np
import uvicorn
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Định nghĩa danh sách các origin được phép
origins = [
    "http://localhost:3000",
]
# Thêm middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Cho phép các origin này
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các phương thức HTTP
    allow_headers=["*"],  # Cho phép tất cả các header
)

MODEL = tf.keras.models.load_model("../saved_models/1.keras")
CLASS_NAMES = ["Early_blight", "Late_blight", "Healthy"]
# @app.get("/ping")
# async def ping():
#     return "Hello"
#

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
    file: UploadFile
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    return {
        'class' : predicted_class,
        'confidence': confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)