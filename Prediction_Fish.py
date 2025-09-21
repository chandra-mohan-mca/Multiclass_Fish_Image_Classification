import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

# Load your trained model
model = load_model('mobilenet_model.h5')

# Define class names (must match your train_generator.class_indices)
class_names = [
    "animal fish", "animal fish bass", "fish sea_food black_sea_sprat", "fish sea_food gilt_head_bream", "fish sea_food hourse_mackerel",
    "fish sea_food red_mullet", "fish sea_food red_sea_bream", "fish sea_food sea_bass", "fish sea_food shrimp", "fish sea_food striped_red_mullet", "fish sea_food trout"
]

st.title("🐟 Fish Classification Prediction")

# Upload image
uploaded_file = st.file_uploader("Upload a fish image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:


    if st.button('Click Predict', key="predict_button"):

        st.balloons()
    # Show uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Preprocess the image
        img = load_img(uploaded_file, target_size=(224, 224))  # Resize to model input size
        img_array = img_to_array(img) / 255.0                 # Normalize to [0, 1]
        img_array = np.expand_dims(img_array, axis=0)         # Add batch dimension

    # Make prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions)

        st.subheader(f"Predicted Class: {class_names[predicted_class]}")
        st.write(f"Confidence: {confidence:.2f}")

    # Show probability distribution
        st.bar_chart(predictions[0])
