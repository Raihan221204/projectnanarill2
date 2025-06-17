from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model("mobilenetv2_wayang_best.h5")
labels = ['Bagong', 'Gareng', 'Petruk', 'Semar']

punakawan_data = {
    "Bagong": {
        "image": "bagong.JPG",
        "description": "Bagong adalah adik bungsu Punakawan, jenaka dan berani.",
        "link": "https://id.wikipedia.org/wiki/Bagong",
        "video": "https://www.youtube.com/watch?v=NAENXVV32CY"
    },
    "Gareng": {
        "image": "gareng.JPG",
        "description": "Gareng dikenal sebagai simbol kesetiaan dan kerendahan hati.",
        "link": "https://id.wikipedia.org/wiki/Gareng",
        "video": "https://www.youtube.com/watch?v=RUI6mVi5XV8"
    },
    "Petruk": {
        "image": "petruk.JPG",
        "description": "Petruk adalah karakter lucu dan cerdas, kritis terhadap keadaan.",
        "link": "https://id.wikipedia.org/wiki/Petruk",
        "video": "https://www.youtube.com/watch?v=58mAG9J6mbE"
    },
    "Semar": {
        "image": "semar.JPG",
        "description": "Semar adalah tokoh bijak dan spiritual dalam Punakawan.",
        "link": "https://id.wikipedia.org/wiki/Semar",
        "video": "https://www.youtube.com/watch?v=1dGbTCmxf2U"
    }
    
}

def preprocess_image(image):
    img = Image.open(image).convert("RGB").resize((224, 224))
    img = np.array(img) / 255.0
    return np.expand_dims(img, axis=0)

def predict_wayang(image):
    img = preprocess_image(image)
    pred = model.predict(img)[0]
    idx = np.argmax(pred)
    label = labels[idx]
    return {"name": label, **punakawan_data[label]}
