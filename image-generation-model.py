import streamlit as st
from PIL import Image
from diffusers import AutoPipelineForImage2Image
from diffusers.utils import make_image_grid

# Load the model and cache it to avoid reloading
@st.cache_resource
def load_pipeline():
    model_id = "stabilityai/stable-diffusion-2-1-base"
    return AutoPipelineForImage2Image.from_pretrained(model_id)

pipeline = load_pipeline()  # Load the cached pipeline

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Center the entire container */
    .main {
        max-width: 800px;
        margin: auto;
    }

    /* Style title and subheading */
    .title {
        text-align: center;
        color: #4F8BF9;
        font-family: Arial, sans-serif;
        font-size: 2.5em;
        font-weight: bold;
        margin-top: 20px;
    }

    .subheading {
        text-align: center;
        color: #6c757d;
        font-size: 1.2em;
        margin-bottom: 30px;
    }

    /* Style the button */
    .stButton > button {
        display: block;
        margin: 0 auto;
        padding: 12px 24px;
        background-color: #4F8BF9;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        border: none;
    }

    /* Customize the file uploader */
    .stFileUploader label {
        font-size: 1em;
        font-weight: bold;
        color: #4F8BF9;
    }

    /* Additional styling */
    .image-container {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }

    /* Style background color */
    .stApp {
        background-color: #f4f4f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page content
st.markdown('<div class="title">🎨 Stable Diffusion Image Generator 🎨</div>', unsafe_allow_html=True)
st.markdown('<div class="subheading">Generate beautiful images from text and initial images</div>', unsafe_allow_html=True)

# Text input for prompt
prompt = st.text_input("Enter a text prompt", "a beautiful collection of fruit in a green environment")

# Image upload section
uploaded_image = st.file_uploader("Upload an initial image", type=["jpg", "png"])

# Generate Image button centered with additional styling
if st.button("Generate Image"):
    if uploaded_image is not None:
        # Process the uploaded image
        init_image = Image.open(uploaded_image).convert("RGB")
        init_image = init_image.resize((512, 512))  

        # Generate the image
        with st.spinner("Generating..."):
            generated_image = pipeline(prompt=prompt, image=init_image).images[0]

        # Display the initial and generated images side by side
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image([init_image, generated_image], caption=["Initial Image", "Generated Image"], use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please upload an initial image first.")
